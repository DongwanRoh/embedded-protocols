# 📚 06. 산업용 필드버스 & 무선 프로토콜

## 📌 1. RS-485 & Modbus
- **RS-485**: 차동 2선(A, B) 기반의 반이중 물리 계층. 최대 32~128개 노드 멀티드롭, 최대 1.2km 전송.
- **Modbus-RTU**:
  - 바이너리 프레임: `[Slave ID (1B)] + [Function Code (1B)] + [Data (NB)] + [CRC16 (2B)]`
  - 3.5 문자 시간의 무신호(Silence)를 프레임 구분자로 사용

## 📌 2. 1-Wire (원와이어)
- 데이터선 1개와 GND만으로 통신 (기생 전원 Parasitic Power 지원)
- Dallas/Maxim 사의 DS18B20 디지털 온도 센서가 대표적
- 마이크로초 단위의 엄격한 타이밍 슬롯으로 비트 구분

## 📌 3. I2S (Inter-IC Sound)
- 디지털 오디오 스트리밍을 위한 전용 3선 시리얼 버스
- SCK (Continuous Serial Clock), WS (Word Select / Left-Right Clock), SD (Serial Data)

## 📌 4. 임베디드 무선 통신
- **BLE (Bluetooth Low Energy)**: GATT 프로파일 기반 Characteristic/Service 모델
- **Zigbee**: 802.15.4 기반 저전력 메시(Mesh) 네트워크
- **LoRa (Long Range)**: CSS 변조 기반 수 km~수십 km 장거리 소량 패킷 전송
- **MQTT**: IoT 경량 발행-구독(Publish-Subscribe) 프로토콜
