# 🛠️ Lab 05. CAN 메시지 인코딩 & 파싱 (CAN Message Parser)

차량용/산업용 CAN 통신에서 주고받는 8바이트 페이로드를 DBC(DataBase CAN) 정의서에 따라 물리값(Physical Value, e.g. RPM, 속도, 배터리 전압)으로 스케일링/오프셋 변환하는 파서를 작성합니다.

---

## 🎯 학습 목표
1. **DBC 신호 변환 공식**:
   $$\text{Physical Value} = (\text{Raw Value} \times \text{Factor}) + \text{Offset}$$
2. **엔디안(Endianness)**:
   - Intel (Little Endian / LSB first)
   - Motorola (Big Endian / MSB first)
3. Python `cantools` 및 `python-can` 라이브러리 활용법
