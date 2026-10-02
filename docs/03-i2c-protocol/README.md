# 📚 03. I2C 프로토콜 (Inter-Integrated Circuit)

## 📌 1. 물리 계층 특징 (Physical Layer)
- **신호선 2개**:
  - **SDA (Serial Data)**: 데이터 입출력 선
  - **SCL (Serial Clock)**: 마스터가 생성하는 동기 클록 선
- **오픈 드레인(Open-Drain) & 풀업 저항(Pull-up Resistor)**:
  - 장치들이 버스를 `Low(GND)`로 당길 수는 있지만, `High`로는 직접 밀어 올리지 못함 (Wired-AND 구조).
  - 통신선에 반드시 **풀업 저항($R_p$)** (보통 2.2kΩ ~ 10kΩ)을 연결해야 함.
  - 버스 충돌 시 쇼트(Short circuit)가 발생하지 않는 구조적 안전성 제공.

---

## 📌 2. 신호 조건 및 프로토콜 시퀀스

```text
       START                  DATA (1 Byte)                    ACK      STOP
SCL  ─────┐      ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐   ┌─────
          └──────┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └──┘  └───┘
SDA  ──┐           ┌──┐        ┌──┐        ┌──┐              ┌──┐       ┌─────
       └───────────┘  └────────┘  └────────┘  └──────────────┘  └───────┘
```

1. **START Condition (S)**: SCL이 High인 상태에서 SDA가 High -> Low로 하강
2. **STOP Condition (P)**: SCL이 High인 상태에서 SDA가 Low -> High로 상승
3. **Data Validity**: SCL이 High인 동안에는 SDA 데이터가 변경되면 안 됨 (안정 유지). SDA는 SCL이 Low일 때만 변경 가능.
4. **ACK / NACK (Acknowledge)**:
   - 8비트 데이터 전송 후 9번째 클록에서 수신기가 SDA를 `Low`로 당기면 **ACK (성공)**
   - 수신기가 SDA를 당기지 않아 `High`로 남아있으면 **NACK (실패 또는 전송 종료)**

---

## 📌 3. 주소 지정 방식 (Addressing)
- **7-bit Address + R/W Bit**:
  - 첫 번째 전송 바이트의 상위 7비트 = 슬레이브 장치 고유 주소
  - 최하위 비트(LSB) = `0`: Write (마스터 -> 슬레이브), `1`: Read (슬레이브 -> 마스터)
- **10-bit Address**: `1111 0XX R/W` 헤더 바이트를 이용한 확장 모드
- **Clock Stretching**: 슬레이브가 데이터 처리 시간이 필요할 때 SCL 라인을 강제로 Low로 붙잡아 마스터의 속도를 늦추는 메커니즘
