---
title: Lab 02. I2C 주소 스캐너 & 레지스터 트랜잭션
description: I2C 버스 주소 스캐닝 및 센서 레지스터 Read/Write 프로토콜 실습
---

## 1. I2C 버스 스캐닝 알고리즘
- 7-bit 주소 범위: `0x08` ~ `0x77` (총 112개 주소)
- 마스터가 각 주소로 START 조건을 걸고 Write 비트 전송 후 ACK 신호가 돌아오는지 확인합니다.

---

## 2. 레지스터 Read 트랜잭션
1. `START` $\rightarrow$ `Slave Address + W` $\rightarrow$ `ACK`
2. `Register Address` $\rightarrow$ `ACK`
3. `REPEATED START` $\rightarrow$ `Slave Address + R` $\rightarrow$ `ACK`
4. `Read Data 1 (ACK)` $\rightarrow$ `Read Data 2 (NACK)` $\rightarrow$ `STOP`
