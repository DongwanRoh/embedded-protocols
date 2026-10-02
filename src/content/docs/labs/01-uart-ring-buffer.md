---
title: Lab 01. UART 원형 버퍼 (Ring Buffer) & 시리얼 모니터
description: C 언어 인터럽트 세이프 링버퍼 구현 및 Python PySerial 모니터링
---

## 1. 링버퍼(Ring Buffer) 개요
UART ISR(인터럽트)이나 DMA 수신 환경에서 수신된 데이터를 손실 없이 메인 루프로 전달하기 위해 FIFO(First-In, First-Out) 구조의 원형 큐를 사용합니다.

```c
typedef struct {
    uint8_t buffer[RING_BUFFER_SIZE];
    volatile size_t head;  // 쓰기 포인터 (ISR에서 증가)
    volatile size_t tail;  // 읽기 포인터 (메인 루프에서 증가)
} RingBuffer;
```

---

## 2. 실습 코드 위치
- C 소스 코드: `labs/01-uart-serial-comms/c_ring_buffer/ring_buffer.c`
- Python 터미널 모니터: `labs/01-uart-serial-comms/python/serial_terminal.py`

```bash
# C 단위 테스트 컴파일 및 실행
gcc -o test labs/01-uart-serial-comms/c_ring_buffer/ring_buffer.c
./test
```
