---
title: 06. 산업용 필드버스 & 무선 프로토콜
description: RS-485 Modbus-RTU, 1-Wire, I2S 디지털 오디오 및 BLE, LoRa, MQTT 정리
---

## 1. RS-485 & Modbus-RTU
- **RS-485**: 차동 2선 기반으로 노이즈에 강하며 최대 1.2km 전송이 가능한 산업용 표준 물리 계층.
- **Modbus-RTU**: `[Slave ID] + [Function Code] + [Data] + [CRC16]` 구조의 마스터-슬레이브 폴링 프로토콜.

## 2. 1-Wire
- 단 1가닥의 신호선과 GND로 통신하는 초소형 센서용 버스 (DS18B20 온도 센서).

## 3. I2S (Inter-IC Sound)
- DAC / ADC / 오디오 코덱 간 무손실 오디오 스트리밍 전용 3선 시리얼 버스.

## 4. 무선 IoT 프로토콜
- **BLE**: 저전력 센서 데이터 수집
- **LoRa**: 수 km 이상 장거리 저속 통신
- **MQTT**: IoT 경량 Pub/Sub 메시징
