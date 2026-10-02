---
title: Lab 04. 시리얼 패킷 프레이밍 & CRC16 검증
description: STX/ETX, 길이 필드, CRC16 체크섬을 갖는 스트리밍 상태 머신(State Machine) 디코더
---

## 1. 패킷 포맷 규격

```text
┌───────┬──────────┬──────────┬──────────┬──────────────┬─────────────┬───────┐
│  STX  │  Length  │  SeqNum  │  Cmd ID  │   Payload    │    CRC16    │  ETX  │
│ (0x02)│ (2 Byte) │ (1 Byte) │ (1 Byte) │  (N Bytes)   │  (2 Bytes)  │ (0x03)│
└───────┴──────────┴──────────┴──────────┴──────────────┴─────────────┴───────┘
```

---

## 2. 상태 머신 (State Machine) 동작 원리
노이즈가 많은 통신 환경에서 바이트가 유실되더라도 `STX(0x02)`가 나타날 때까지 대기하고, CRC16 체크섬을 통해 페이로드의 무결성을 검증합니다.

```bash
# 파이썬 코덱 테스트 실행
python labs/04-custom-packet-framing/packet_codec.py
```
