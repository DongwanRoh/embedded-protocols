# 🔌 Embedded Protocols (`embedded-protocols`)

> **임베디드 시스템 및 하드웨어 통신 프로토콜(UART, I2C, SPI, CAN 등)의 동작 원리 분석, 회로 특성 이해 및 펌웨어/드라이버 구현 실습 저장소**

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/DongwanRoh/embedded-protocols/pulls)

---

## 🎯 프로젝트 목표 (Goals)

1. **하드웨어 인터페이스 물리 계층 이해**: 전압 레벨(TTL, RS-232, 차동 신호), 오픈 드레인(Open-Drain), 풀업 저항, 클록 동기화 등 전기적 특성 완벽 파악
2. **타이밍 다이어그램 & 프레임 분석**: 오실로스코프 및 로직 아날라이저(Logic Analyzer) 관점에서의 비트 타이밍 및 패킷 파싱
3. **신뢰성 높은 통신 드라이버 구현**: 인터럽트(Interrupt), 원형 버퍼(Circular/Ring Buffer), DMA, CRC 체크섬, 커스텀 패킷 프레이밍 기법 습득

---

## 📊 주요 임베디드 시리얼 프로토콜 비교

| 프로토콜 | 동기/비동기 | 통신 방식 | 핀(Line) 수 | 최대 속도(일반적) | 토폴로지 | 대표 용도 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **UART / USART** | 비동기 (USART는 동기 가능) | 전이중 (Full-Duplex) | 2개 (TX, RX) | ~115.2 kbps / ~1+ Mbps | 1:1 Point-to-Point | 디버그 콘솔, 블루투스/GPS 모듈, RS-485 |
| **I2C** | 동기 (Synchronous) | 반이중 (Half-Duplex) | 2개 (SDA, SCL) | 100 kbps / 400 kbps / 3.4 Mbps | 1:N (다중 슬레이브/다중 마스터) | 온습도/가속도 센서, EEPROM, RTC, OLED |
| **SPI** | 동기 (Synchronous) | 전이중 (Full-Duplex) | 4개 (MOSI, MISO, SCK, CS) | 10 Mbps ~ 50+ Mbps | 1:N (개별 CS 핀 또는 데이지 체인) | 플래시 메모리, SD 카드, TFT LCD, 고속 ADC |
| **CAN / CAN-FD** | 비동기 (차동 신호) | 반이중 (Half-Duplex) | 2개 (CAN_H, CAN_L) | 1 Mbps (CAN) / 5~8 Mbps (FD) | Multi-Master 버스 | 자동차 전장 부품, 산업용 자동화 제어 |

---

## 🗂️ 프로젝트 디렉토리 구조 (Directory Structure)

```text
embedded-protocols/
├── docs/                                      # 📚 하드웨어 통신 프로토콜 이론 및 신호 분석
│   ├── 01-serial-communication-fundamentals/  # 시리얼 통신 기초 (동기/비동기, 전이중/반이중, 보드레이트, TTL vs RS232)
│   ├── 02-uart-usart/                         # UART/USART (프레임 구조, 하드웨어 플로우 제어, 링버퍼/DMA 수신)
│   ├── 03-i2c-protocol/                       # I2C (SDA/SCL, 오픈드레인, 풀업저항, Start/Stop 조건, ACK/NACK, 7/10비트 주소)
│   ├── 04-spi-protocol/                       # SPI (4-Wire, CPOL/CPHA 4가지 모드, CS 제어, 고속 전송 최적화)
│   ├── 05-can-bus/                            # CAN Bus (차동신호, 종단저항 120Ω, 메시지 ID 중재, Error Frame, CAN-FD)
│   └── 06-industrial-and-wireless/            # RS-485/Modbus, 1-Wire, I2S(오디오), BLE, LoRa
│
└── labs/                                      # 🛠️ 실습 코드 및 패킷 파서 구현체
    ├── 01-uart-serial-comms/                  # PC-MCU 시리얼 통신, 링버퍼(Ring Buffer) 구현
    ├── 02-i2c-device-driver/                  # I2C 버스 스캐너 및 센서 레지스터 Read/Write 로직
    ├── 03-spi-driver/                         # SPI Flash 메모리 / 디스플레이 패킷 제어
    ├── 04-custom-packet-framing/              # STX/ETX, Header-Payload, CRC16/CRC32 프레이밍 엔진
    └── 05-can-message-parser/                 # CAN DBC 파일 분석 및 메시지 인코딩/디코딩
```

---

## 🗺️ 상세 학습 로드맵

### Phase 1: 시리얼 통신 기본기 (UART & RS-232 / RS-485)
- [ ] Baud rate와 비트 샘플링(Oversampling 16x) 원리
- [ ] UART 프레임 구성 (Start 1bit, Data 7/8bits, Parity None/Odd/Even, Stop 1/2bits)
- [ ] 하드웨어 흐름 제어(RTS/CTS) 및 소프트웨어 흐름 제어(XON/XOFF)
- [ ] 펌웨어 수신 방식 비교: 폴링(Polling) vs 인터럽트(Interrupt) vs DMA(Direct Memory Access)
- [ ] **[Lab 01]** Python `pyserial` 및 C 언어 원형 큐(Circular Ring Buffer) 구현

### Phase 2: 온보드 버스 통신 (I2C & SPI)
- [ ] **I2C**:
  - Open-Drain 출력과 Pull-up 저항 크기 계산 ($R_p = \frac{t_r}{0.8473 \times C_b}$)
  - START, STOP, REPEATED START 조건과 데이터 홀드/셋업 타임
  - 7-bit / 10-bit 슬레이브 주소 지정 및 R/W 비트
  - Clock Stretching (슬레이브의 클록 홀딩) 메커니즘
- [ ] **SPI**:
  - 클록 극성(CPOL)과 위상(CPHA)에 따른 Mode 0 (0,0), Mode 1 (0,1), Mode 2 (1,0), Mode 3 (1,1)
  - 칩 셀렉트(CS/SS) 멀티플렉싱 및 데이지 체인(Daisy Chain) 연결 방식
- [ ] **[Lab 02 & 03]** I2C 주소 스캐너 및 SPI 레지스터 트랜잭션 드라이버 구현

### Phase 3: 견고한 통신 및 필드버스 (CAN & Industrial Comms)
- [ ] 노이즈 억제를 위한 차동 신호(Differential Signaling: $V_{diff} = CAN\_H - CAN\_L$)
- [ ] 비트 와이어링(Wired-AND) 및 비파괴 비트 단위 중재(Arbitration)
- [ ] 비트 스터핑(Bit Stuffing)과 에러 프레임 감지
- [ ] Modbus-RTU (RS-485 기반 마스터-슬레이브 폴링)
- [ ] **[Lab 04 & 05]** CRC 체크섬 검증을 포함한 패킷 직렬화 프레이밍 엔진 구현

---

## 🚀 빠른 시작 (Getting Started)

원하는 실습 디렉토리로 이동하여 실습 가이드를 확인하세요.

```bash
# 저장소 클론
git clone https://github.com/DongwanRoh/embedded-protocols.git
cd embedded-protocols

# 1번 UART/Serial 실습 확인
cd labs/01-uart-serial-comms
```

---

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
