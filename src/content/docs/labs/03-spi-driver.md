---
title: Lab 03. SPI 플래시 메모리 (W25Qxx) 드라이버
description: SPI Flash 메모리 명령어 집합(JEDEC ID, Read, Write Enable, Sector Erase) 구현
---

## 1. W25Qxx SPI 명령 시퀀스
- `CS Low` 활성화 $\rightarrow$ 명령어 전송 $\rightarrow$ 데이터 수신 $\rightarrow$ `CS High`

| 명령어 | Hex 코드 | 설명 |
| :--- | :---: | :--- |
| **Read JEDEC ID** | `0x9F` | 제조사(Winbond: 0xEF) 및 장치 ID 3바이트 반환 |
| **Write Enable** | `0x06` | 쓰기/지우기 전 WEL(Write Enable Latch) 비트 활성화 |
| **Read Data** | `0x03` | 24비트 주소 전송 후 데이터 스트리밍 |
| **Sector Erase** | `0x20` | 지정된 4KB 섹터 영역 0xFF로 초기화 |
