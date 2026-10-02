# 📚 04. SPI 프로토콜 (Serial Peripheral Interface)

## 📌 1. 물리 핀 구성 (4-Wire)
1. **MOSI (Master Out Slave In)**: 마스터에서 슬레이브로 데이터 전송
2. **MISO (Master In Slave Out)**: 슬레이브에서 마스터로 데이터 전송
3. **SCK (Serial Clock)**: 마스터가 생성하는 고속 동기 클록 (수십 MHz 가능)
4. **CS / SS (Chip Select / Slave Select)**: 활성화할 슬레이브를 선택하는 `Active-Low` 신호

---

## 📌 2. SPI 4가지 모드 (CPOL & CPHA)

- **CPOL (Clock Polarity)**: 유휴(Idle) 상태에서의 클록 레벨
  - `0`: Idle = Low
  - `1`: Idle = High
- **CPHA (Clock Phase)**: 데이터를 샘플링(캡처)하는 클록 에지
  - `0`: 첫 번째 에지(First Edge)에서 샘플링
  - `1`: 두 번째 에지(Second Edge)에서 샘플링

| SPI Mode | CPOL | CPHA | Clock Idle | 샘플링 에지 (Data Sampling) |
| :---: | :---: | :---: | :---: | :---: |
| **Mode 0** | 0 | 0 | Low | Rising Edge (상승) |
| **Mode 1** | 0 | 1 | Low | Falling Edge (하강) |
| **Mode 2** | 1 | 0 | High | Falling Edge (하강) |
| **Mode 3** | 1 | 1 | High | Rising Edge (상승) |

> 💡 **Mode 0**과 **Mode 3**이 실제 상용 센서 및 Flash 메모리에서 가장 흔히 사용됩니다.

---

## 📌 3. I2C vs SPI 비교
- **SPI의 장점**: 프로토콜 오버헤드(주소 비트, ACK 비트 등)가 전혀 없어 매우 빠름(50MHz+), 동시 송수신(Full-Duplex) 가능
- **SPI의 단점**: 슬레이브가 늘어날 때마다 CS 핀이 1개씩 추가로 필요 (포트 낭비), ACK 응답이 없어 데이터 수신 여부 확인을 소프트웨어 레벨에서 구현해야 함
