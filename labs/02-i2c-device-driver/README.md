# 🛠️ Lab 02. I2C 버스 스캐너 및 센서 드라이버 (I2C Scanner & Driver)

I2C 버스에 연결된 모든 슬레이브 장치의 7-bit 주소(`0x08` ~ `0x77`)로 ACK 응답을 확인하여 주소를 탐색하는 I2C 스캐너와, 대표적인 I2C 센서(EEPROM, 온습도 센서 SHT31/AHT20, OLED SSD1306 등)의 레지스터 Read/Write 프로토콜을 다룹니다.

---

## 🎯 학습 목표
1. I2C 주소 스캐닝 알고리즘 (Start -> `(Address << 1) | Write` -> ACK 확인 -> Stop)
2. 레지스터 포인터 기반 트랜잭션:
   - **Write**: `[Device Addr (W)] + [Register Addr] + [Data 1] + [Data 2] ...`
   - **Read**: `[Device Addr (W)] + [Register Addr]` -> `[Repeated START]` -> `[Device Addr (R)]` -> `[Read Data...]`
3. 아두이노 `Wire.h`, STM32 `HAL_I2C_Mem_Read/Write`, Python `smbus2` 사용법
