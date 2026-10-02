# 📚 05. CAN 버스 (Controller Area Network)

## 📌 1. 물리 계층과 차동 신호 (Differential Signaling)
- **CAN_H (High)** 와 **CAN_L (Low)** 두 선의 전압 차이($V_{diff}$)로 비트 결정
- **우성 비트 (Dominant, Logic 0)**: $V_{diff} \approx 2.0V$ (CAN_H: 3.5V, CAN_L: 1.5V)
- **열성 비트 (Recessive, Logic 1)**: $V_{diff} \approx 0V$ (CAN_H: 2.5V, CAN_L: 2.5V)
- ⚠️ **우성 비트(0)가 열성 비트(1)를 항상 이깁니다 (Wired-AND).**
- 버스 양 끝단에 **120Ω 종단 저항(Termination Resistor)** 필수 (합성 저항 60Ω)

---

## 📌 2. 비파괴 비트 단위 중재 (Non-Destructive Bitwise Arbitration)
- 마스터가 없는 Multi-Master 구조.
- 여러 노드가 동시에 메시지를 송신할 때, **메시지 식별자(Identifier / CAN ID)** 값이 **가장 작은 노드(우성 비트 '0'이 더 많은 노드)** 가 버스 점유권을 획득.
- ID 번호가 작을수록 우선순위(Priority)가 높음.

---

## 📌 3. 프레임 종류
1. **Data Frame**: 실제 센서/제어 데이터 전송 (CAN 2.0A: 11-bit ID, CAN 2.0B: 29-bit Extended ID, 최대 8바이트 데이터 / CAN-FD: 최대 64바이트)
2. **Remote Frame**: 다른 노드에 데이터 송신 요청
3. **Error Frame**: 노이즈, CRC 불일치, 비트 스터핑 에러 감지 시 즉시 브로드캐스트
4. **Overload Frame**: 수신 노드가 버퍼 처리가 늦을 때 지연 요청
