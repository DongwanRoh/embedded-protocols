#include "ring_buffer.h"
#include <stdio.h>
#include <assert.h>

void ring_buffer_init(RingBuffer *rb) {
    if (!rb) return;
    rb->head = 0;
    rb->tail = 0;
}

bool ring_buffer_is_empty(const RingBuffer *rb) {
    return (rb->head == rb->tail);
}

bool ring_buffer_is_full(const RingBuffer *rb) {
    return ((rb->head + 1) % RING_BUFFER_SIZE) == rb->tail;
}

size_t ring_buffer_available_data(const RingBuffer *rb) {
    if (rb->head >= rb->tail) {
        return rb->head - rb->tail;
    }
    return RING_BUFFER_SIZE - (rb->tail - rb->head);
}

size_t ring_buffer_available_space(const RingBuffer *rb) {
    return (RING_BUFFER_SIZE - 1) - ring_buffer_available_data(rb);
}

bool ring_buffer_push(RingBuffer *rb, uint8_t byte) {
    if (ring_buffer_is_full(rb)) {
        // 버퍼가 꽉 찼을 경우 오버플로우 처리 (실패 반환 또는 덮어쓰기 정책)
        return false;
    }
    rb->buffer[rb->head] = byte;
    rb->head = (rb->head + 1) % RING_BUFFER_SIZE;
    return true;
}

bool ring_buffer_pop(RingBuffer *rb, uint8_t *byte) {
    if (ring_buffer_is_empty(rb)) {
        return false;
    }
    if (byte) {
        *byte = rb->buffer[rb->tail];
    }
    rb->tail = (rb->tail + 1) % RING_BUFFER_SIZE;
    return true;
}

// ----------------------------------------------------------------------------
// Unit Test
// ----------------------------------------------------------------------------
int main(void) {
    printf("[RingBuffer Test] Starting circular buffer verification...\n");
    RingBuffer rb;
    ring_buffer_init(&rb);

    assert(ring_buffer_is_empty(&rb) == true);
    assert(ring_buffer_available_data(&rb) == 0);

    // 1. 데이터 삽입 테스트
    for (uint8_t i = 0; i < 10; i++) {
        bool ok = ring_buffer_push(&rb, i * 10);
        assert(ok == true);
    }
    assert(ring_buffer_available_data(&rb) == 10);

    // 2. 데이터 인출 및 검증
    for (uint8_t i = 0; i < 10; i++) {
        uint8_t val;
        bool ok = ring_buffer_pop(&rb, &val);
        assert(ok == true);
        assert(val == i * 10);
    }
    assert(ring_buffer_is_empty(&rb) == true);

    printf("[RingBuffer Test] All assertions passed successfully! ✅\n");
    return 0;
}
