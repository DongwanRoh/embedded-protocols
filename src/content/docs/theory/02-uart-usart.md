---
title: 02. UART & USART 프로토콜
description: 비동기 시리얼 통신 프레임 포맷, 하드웨어 플로우 제어, MCU 인터럽트/DMA 수신 아키텍처
---

## 1. UART 프레임 구조 (Frame Format)

UART는 별도의 클록 선이 없으므로, 데이터 라인이 유휴(Idle) 상태일 때는 항상 **High(Logic 1)** 를 유지합니다.

```text
       ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
IDLE ──┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └─── IDLE
       START   D0      D1      D2      D3      D4      D5      D6      D7/PARITY STOP
        (0)   (LSB)                                            (MSB)       (1)
```

1. **Start Bit (1비트)**: 통신의 시작을 알리는 `Low(0)` 신호입니다.
2. **Data Bits (5~9비트, 보통 8비트)**: LSB(Least Significant Bit)부터 차례로 전송됩니다.
3. **Parity Bit (선택, 0/1비트)**: None, Even, Odd 방식으로 1비트 에러를 검출합니다.
4. **Stop Bit (1, 1.5, 2비트)**: 프레임의 끝을 알리는 `High(1)` 신호입니다.

---

## 2. 하드웨어 흐름 제어 (Hardware Flow Control)
수신 측 MCU의 버퍼가 가득 차서 데이터가 유실(Overrun Error)되는 것을 방지하기 위해 사용합니다.
- **RTS (Request to Send)**: 송신 측이 수신 측에 데이터를 보낼 준비가 되었는지 묻는 신호
- **CTS (Clear to Send)**: 수신 측이 수신할 준비가 되었을 때 활성화하는 신호

---

## 3. MCU 펌웨어 수신 아키텍처 비교

1. **Polling (폴링 방식)**: CPU가 `RXNE` 플래그를 계속 검사. 단순하지만 CPU 낭비가 심함.
2. **Interrupt + Ring Buffer (인터럽트 방식)**: 1바이트 수신 시마다 ISR에서 원형 큐(Ring Buffer)로 데이터를 복사.
3. **DMA + IDLE Line Interrupt (가장 추천)**: CPU 개입 없이 메모리로 직접 블록 수신하고, 한 프레임 전송이 끝나는 IDLE 라인 감지 시 1회만 인터럽트 발생.
