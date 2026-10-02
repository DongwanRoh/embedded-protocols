#ifndef RING_BUFFER_H
#define RING_BUFFER_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#define RING_BUFFER_SIZE 256  // 2의 거듭제곱 권장 (비트 연산 최적화 가능)

typedef struct {
    uint8_t buffer[RING_BUFFER_SIZE];
    volatile size_t head;  // 데이터를 쓰는 인덱스 (Write)
    volatile size_t tail;  // 데이터를 읽는 인덱스 (Read)
} RingBuffer;

void ring_buffer_init(RingBuffer *rb);
bool ring_buffer_is_empty(const RingBuffer *rb);
bool ring_buffer_is_full(const RingBuffer *rb);
size_t ring_buffer_available_data(const RingBuffer *rb);
size_t ring_buffer_available_space(const RingBuffer *rb);

bool ring_buffer_push(RingBuffer *rb, uint8_t byte);
bool ring_buffer_pop(RingBuffer *rb, uint8_t *byte);

#endif // RING_BUFFER_H
