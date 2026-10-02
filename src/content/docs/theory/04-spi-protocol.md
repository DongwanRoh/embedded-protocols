---
title: 04. SPI 프로토콜 (Serial Peripheral Interface)
description: 4-Wire 고속 전이중 인터페이스, CPOL 및 CPHA 모드 0~3, CS 제어 방식
---

## 1. 물리 핀 구성 (4-Wire)
- **MOSI (Master Out Slave In)**: 마스터 $\rightarrow$ 슬레이브 데이터 송신
- **MISO (Master In Slave Out)**: 슬레이브 $\rightarrow$ 마스터 데이터 수신
- **SCK (Serial Clock)**: 마스터가 제공하는 동기 클록 (수십 MHz 가능)
- **CS / SS (Chip Select / Slave Select)**: 특정 슬레이브를 활성화하는 Active-Low 신호

---

## 2. SPI 4가지 모드 (CPOL & CPHA)

- **CPOL (Clock Polarity)**: 유휴(Idle) 상태의 클록 레벨 (`0: Low`, `1: High`)
- **CPHA (Clock Phase)**: 데이터 샘플링 에지 (`0: 첫 번째 에지`, `1: 두 번째 에지`)

| SPI 모드 | CPOL | CPHA | Clock Idle | 데이터 샘플링 타이밍 |
| :---: | :---: | :---: | :---: | :---: |
| **Mode 0** | 0 | 0 | Low | 상승 에지 (Rising Edge) |
| **Mode 1** | 0 | 1 | Low | 하강 에지 (Falling Edge) |
| **Mode 2** | 1 | 0 | High | 하강 에지 (Falling Edge) |
| **Mode 3** | 1 | 1 | High | 상승 에지 (Rising Edge) |

> 💡 **Mode 0**과 **Mode 3**이 플래시 메모리, SD 카드, 센서 등에서 가장 널리 사용됩니다.
