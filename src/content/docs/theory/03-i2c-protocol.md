---
title: 03. I2C 프로토콜 (Inter-Integrated Circuit)
description: SDA/SCL 2선식 버스, 오픈 드레인 & 풀업 저항, START/STOP 조건, 7비트 주소 체계 및 ACK/NACK
---

## 1. 물리 계층: 오픈 드레인(Open-Drain) & 풀업 저항

I2C는 단 2가닥의 선으로 통신합니다:
- **SDA (Serial Data)**: 데이터 입출력 선
- **SCL (Serial Clock)**: 동기 클록 선

모든 I2C 디바이스의 핀은 **오픈 드레인(Open-Drain)** 구조로 되어 있어, 버스를 `Low(0V)`로 끌어내릴 수만 있고 `High(VCC)`로 밀어 올리지는 못합니다. 따라서 버스 라인에 반드시 **풀업 저항(Pull-up Resistor)** 을 달아주어야 합니다.

---

## 2. 통신 시퀀스 & 신호 조건

```text
       START                  DATA (1 Byte)                    ACK      STOP
SCL  ─────┐      ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐   ┌─────
          └──────┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └───┘
SDA  ──┐           ┌──┐        ┌──┐        ┌──┐              ┌──┐       ┌─────
       └───────────┘  └────────┘  └────────┘  └──────────────┘  └───────┘
```

1. **START 조건**: SCL이 High인 동안 SDA가 High $\rightarrow$ Low로 하강
2. **STOP 조건**: SCL이 High인 동안 SDA가 Low $\rightarrow$ High로 상승
3. **Data 유효성**: SCL이 High인 동안 SDA 레벨은 반드시 고정되어야 함 (SCL이 Low일 때만 변경 가능)
4. **ACK / NACK**: 8비트 데이터 전송 후 9번째 클록에서 수신기가 SDA를 Low로 당기면 ACK(성공), 당기지 않으면 NACK(실패/종료)

---

## 3. 7비트 주소 체계와 R/W 비트
- 통신의 첫 바이트는 `[7-bit Slave Address] + [1-bit R/W]`로 구성됩니다.
  - `R/W = 0`: 마스터가 슬레이브에 데이터 쓰기 (Write)
  - `R/W = 1`: 마스터가 슬레이브로부터 데이터 읽기 (Read)
