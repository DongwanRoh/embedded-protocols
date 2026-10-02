"""
Robust Serial Packet Framing & Parsing State Machine with CRC16-CCITT
"""
import struct
from enum import Enum, auto
from typing import Optional, List, NamedTuple

STX = 0x02  # Start of Text
ETX = 0x03  # End of Text

def calculate_crc16_ccitt(data: bytes, poly: int = 0x1021, init_val: int = 0xFFFF) -> int:
    """CRC16-CCITT (Poly: 0x1021, Init: 0xFFFF)"""
    crc = init_val
    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ poly) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return crc

class Packet(NamedTuple):
    seq: int
    cmd: int
    payload: bytes

class PacketEncoder:
    @staticmethod
    def encode(seq: int, cmd: int, payload: bytes) -> bytes:
        length = len(payload)
        # Header + Payload
        header_and_data = struct.pack(">HBB", length, seq, cmd) + payload
        crc = calculate_crc16_ccitt(header_and_data)
        # STX + [Header + Payload + CRC16] + ETX
        return bytes([STX]) + header_and_data + struct.pack(">H", crc) + bytes([ETX])

class State(Enum):
    WAIT_STX = auto()
    READ_LENGTH_H = auto()
    READ_LENGTH_L = auto()
    READ_SEQ = auto()
    READ_CMD = auto()
    READ_PAYLOAD = auto()
    READ_CRC_H = auto()
    READ_CRC_L = auto()
    WAIT_ETX = auto()

class PacketDecoder:
    """Byte-by-byte streaming state machine parser (ideal for UART ISR / RingBuffer)"""
    def __init__(self):
        self.state = State.WAIT_STX
        self.length = 0
        self.seq = 0
        self.cmd = 0
        self.payload = bytearray()
        self.crc_received = 0
        self.raw_data_for_crc = bytearray()

    def process_byte(self, byte: int) -> Optional[Packet]:
        if self.state == State.WAIT_STX:
            if byte == STX:
                self.state = State.READ_LENGTH_H
                self.raw_data_for_crc.clear()
                self.payload.clear()

        elif self.state == State.READ_LENGTH_H:
            self.length = byte << 8
            self.raw_data_for_crc.append(byte)
            self.state = State.READ_LENGTH_L

        elif self.state == State.READ_LENGTH_L:
            self.length |= byte
            self.raw_data_for_crc.append(byte)
            self.state = State.READ_SEQ

        elif self.state == State.READ_SEQ:
            self.seq = byte
            self.raw_data_for_crc.append(byte)
            self.state = State.READ_CMD

        elif self.state == State.READ_CMD:
            self.cmd = byte
            self.raw_data_for_crc.append(byte)
            if self.length > 0:
                self.state = State.READ_PAYLOAD
            else:
                self.state = State.READ_CRC_H

        elif self.state == State.READ_PAYLOAD:
            self.payload.append(byte)
            self.raw_data_for_crc.append(byte)
            if len(self.payload) == self.length:
                self.state = State.READ_CRC_H

        elif self.state == State.READ_CRC_H:
            self.crc_received = byte << 8
            self.state = State.READ_CRC_L

        elif self.state == State.READ_CRC_L:
            self.crc_received |= byte
            self.state = State.WAIT_ETX

        elif self.state == State.WAIT_ETX:
            self.state = State.WAIT_STX
            if byte == ETX:
                expected_crc = calculate_crc16_ccitt(bytes(self.raw_data_for_crc))
                if self.crc_received == expected_crc:
                    return Packet(seq=self.seq, cmd=self.cmd, payload=bytes(self.payload))
                else:
                    print(f"[Decoder Error] CRC Mismatch! Expected 0x{expected_crc:04X}, Got 0x{self.crc_received:04X}")
            else:
                print(f"[Decoder Error] Expected ETX(0x03), Got 0x{byte:02X}")
        return None

if __name__ == "__main__":
    print("=== Packet Framing & Decoder Test ===")
    encoder = PacketEncoder()
    decoder = PacketDecoder()

    # 테스트 패킷 생성
    test_payload = "Sensor_Temp:25.4C,Hum:60%".encode("utf-8")
    encoded_frame = encoder.encode(seq=1, cmd=0xA1, payload=test_payload)
    print(f"Encoded Hex Stream ({len(encoded_frame)} bytes):")
    print(" ".join(f"{b:02X}" for b in encoded_frame))

    # 노이즈 바이트 삽입 시뮬레이션
    noisy_stream = b"\xFF\xEE" + encoded_frame + b"\xAA"

    received_packets: List[Packet] = []
    for b in noisy_stream:
        pkt = decoder.process_byte(b)
        if pkt:
            received_packets.append(pkt)

    assert len(received_packets) == 1
    decoded = received_packets[0]
    print(f"\nSuccessfully Decoded Packet:")
    print(f"- Seq: {decoded.seq}")
    print(f"- Cmd: 0x{decoded.cmd:02X}")
    print(f"- Payload: {decoded.payload.decode('utf-8')}")
    print("\nAll Packet Framing Tests Passed! ✅")
