# 🛠️ Lab 01. UART 시리얼 통신 & 원형 버퍼 (Ring Buffer)

임베디드 펌웨어에서 UART 데이터를 끊김 없이 안전하게 수신하기 위해 가장 널리 쓰이는 **원형 버퍼(Circular/Ring Buffer)** C 언어 구현과, PC에서 시리얼 포트를 열고 테스트할 수 있는 Python 스크립트입니다.

---

## 🎯 학습 목표
1. 인터럽트/DMA 환경에서 레이스 컨디션 없이 바이트를 보관하는 락-프리(Lock-free) 원형 버퍼 설계
2. 오버런(Overrun / Buffer Full) 처리 전략
3. Python `pyserial`을 이용한 보레이트 설정 및 Hex 데이터 송수신

---

## 📂 파일 구성
- `c_ring_buffer/ring_buffer.h`: 링버퍼 헤더
- `c_ring_buffer/ring_buffer.c`: 링버퍼 삽입/인출/크기 계산 로직 및 유닛 테스트
- `python/serial_terminal.py`: 터미널 기반 시리얼 포트 모니터

---

## 🚀 C 링버퍼 테스트 빌드 & 실행
```bash
# gcc로 컴파일 및 실행
gcc -o ring_buffer_test c_ring_buffer/ring_buffer.c
./ring_buffer_test
```
