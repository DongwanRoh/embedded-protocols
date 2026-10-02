---
title: 01. 시리얼 통신 기초 (Serial Communication Fundamentals)
description: 패러럴 vs 시리얼 비교, 통신 방향, 클록 동기화 및 물리 계층 전기적 신호 규격 정리
---

## 1. 패러럴(Parallel) vs 시리얼(Serial) 통신

### 패러럴 통신 (Parallel)
- **개념**: 여러 개의 데이터 선(Data Bus)을 통해 한 번에 다수의 비트(8, 16, 32, 64bit 등)를 동시에 전송합니다.
- **단점**: 선로 간 신호 왜곡(Skew), 고주파에서의 누화(Crosstalk), PCB 배선 및 핀 수 증가로 인해 고속/장거리 전송에 불리합니다.

### 시리얼 통신 (Serial)
- **개념**: 단일 데이터 선(또는 차동 2선)을 통해 시간 순서대로 1비트씩 직렬 전송합니다.
- **장점**: 적은 핀 수, 높은 노이즈 내성, 고속화 용이 (오늘날 PCIe, USB, SATA, UART, I2C, SPI 등 대부분의 고속 인터페이스가 시리얼을 채택).

---

## 2. 통신 방식 분류

### 1) 데이터 전송 방향 (Directionality)
1. **단방향 (Simplex)**: 한쪽 방향으로만 송신합니다. (예: 라디오 수신, 단순 GPS NMEA 센서 출력)
2. **반이중 (Half-Duplex)**: 양방향 통신이 가능하지만, 같은 시점에 동시 전송은 불가합니다. (예: 무전기, I2C, RS-485, CAN)
3. **전이중 (Full-Duplex)**: 송신선과 수신선이 분리되어 있어 동시에 양방향 전송이 가능합니다. (예: 전화기, UART, SPI, Ethernet)

### 2) 클록 동기화 방식 (Clock Synchronization)
- **동기식 (Synchronous)**: 송수신기가 **클록(Clock, SCK)** 라인을 공유하여 클록 에지에 맞춰 비트를 정확히 샘플링합니다. (예: I2C, SPI, I2S)
- **비동기식 (Asynchronous)**: 별도의 클록 라인이 없으며, 사전에 약속된 **통신 속도(Baud Rate)** 와 시작/정지(Start/Stop) 비트로 타이밍을 동기화합니다. (예: UART, CAN)

---

## 3. 물리 계층 전기적 신호 규격

| 규격 | 신호 방식 | 전압 레벨 (Logic 0 / Logic 1) | 최대 거리 | 최대 속도 |
| :--- | :--- | :--- | :--- | :--- |
| **TTL (MCU Level)** | Single-Ended | 0V (Low) / 3.3V 또는 5V (High) | < 1 m | ~수 Mbps |
| **RS-232** | Single-Ended (Inverted) | +3V ~ +15V (0) / -3V ~ -15V (1) | ~15 m | ~115.2 kbps |
| **RS-485** | Differential (차동 신호) | $V_A - V_B < -200\text{mV}$ (0) / $> +200\text{mV}$ (1) | ~1.2 km | ~10 Mbps |
