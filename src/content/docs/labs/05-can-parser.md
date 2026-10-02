---
title: Lab 05. CAN 메시지 인코딩 & DBC 파싱
description: CAN 8바이트 페이로드 신호 스케일링 및 엔디안 변환기
---

## 1. DBC 변환 공식
$$\text{Physical Value} = (\text{Raw Value} \times \text{Factor}) + \text{Offset}$$

## 2. 엔디안(Endianness) 주의점
- **Intel (Little Endian)**: LSB가 앞선 비트/바이트에 위치
- **Motorola (Big Endian)**: MSB가 앞선 비트/바이트에 위치
