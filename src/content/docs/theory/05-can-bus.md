---
title: 05. CAN 버스 (Controller Area Network)
description: 차량용/산업용 CAN Bus 차동 신호, 종단 저항 120Ω, 비트 단위 중재 및 에러 처리
---

## 1. 차동 신호 (Differential Signaling)
- **CAN_H**와 **CAN_L**의 전압차($V_{diff} = CAN\_H - CAN\_L$)로 논리 비트를 판정합니다.
- **우성 비트 (Dominant, Logic 0)**: $V_{diff} \approx 2.0V$
- **열성 비트 (Recessive, Logic 1)**: $V_{diff} \approx 0.0V$
- 버스 상에서 **우성 비트(0)가 항상 열성 비트(1)를 이깁니다 (Wired-AND)**.
- 반사파 제거를 위해 버스 양 끝단에 **120Ω 종단 저항(Termination Resistor)** 을 연결합니다.

---

## 2. 비트 단위 비파괴 중재 (Arbitration)
- 여러 노드가 동시에 메시지를 전송할 때, **식별자(CAN ID)의 숫자가 더 작은 노드(우성 비트 '0'이 더 많은 노드)** 가 버스 점유권을 획득합니다.
- 즉, **ID 번호가 작을수록 높은 우선순위(Priority)** 를 갖습니다.
