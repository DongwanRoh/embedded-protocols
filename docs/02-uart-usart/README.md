# 📚 02. UART & USART (Universal Asynchronous/Synchronous Receiver-Transmitter)

## 📌 1. UART 프레임 구조 (Frame Format)

기본 유휴 상태(Idle)는 **High(1)** 상태를 유지합니다.

```text
       ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
IDLE ──┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └───┘   └─── IDLE
       START   D0      D1      D2      D3      D4      D5      D6      D7/PARITY STOP
        (0)   (LSB)                                            (MSB)       (1)
```

1. **Start Bit (1비트)**: 통신의 시작을 알리는 `Low(0)` 신호. 수신기의 오버샘플링 클록을 리셋하고 동기화.
2. **Data Bits (5~9비트, 보통 8비트)**: LSB(Least Significant Bit)부터 순차 전송.
3. **Parity Bit (옵션, 0 또는 1비트)**: None, Even(짝수), Odd(홀수) 패리티로 1비트 오류 검출.
4. **Stop Bit (1, 1.5, 2비트)**: 프레임의 종료를 알리는 `High(1)` 신호. 수신기가 다음 프레임을 준비할 수 있는 시간 제공.
> 가장 널리 쓰이는 표준 포맷: **8-N-1** (8 Data bits, No parity, 1 Stop bit)

---

## 📌 2. 하드웨어 흐름 제어 (Flow Control)
- 수신 버퍼 오버플로우(Buffer Overflow)를 방지하기 위해 송수신 상태를 제어:
  - **RTS (Request to Send)**: 송신 측이 수신 측에 데이터 송신 준비 여부 문의
  - **CTS (Clear to Send)**: 수신 측이 수신 가능 상태일 때 송신 측에 신호 전달

---

## 📌 3. MCU 펌웨어 수신 아키텍처
1. **Polling (폴링)**: CPU가 플래그(`RXNE`)를 계속 확인. CPU 점유율 낭비.
2. **Interrupt (인터럽트)**: 1바이트 수신마다 ISR(인터럽트 서비스 루틴) 발생 -> **원형 큐(Circular Ring Buffer)** 에 저장.
3. **DMA (Direct Memory Access) + Idle Line Interrupt**: CPU 개입 없이 메모리로 직접 블록 단위 전송. 수신 완료 시 한 번만 인터럽트 발생(가장 이상적인 고속 수신 방식).
