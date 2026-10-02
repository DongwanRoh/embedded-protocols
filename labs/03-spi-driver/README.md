# 🛠️ Lab 03. SPI 메모리 & 디스플레이 드라이버 (SPI Driver)

대표적인 SPI 장치인 **NOR Flash (W25Qxx 시리즈)** 와 **TFT LCD (ST7789/ILI9341)** 제어 프로토콜을 구현합니다.

---

## 🎯 학습 목표
1. **SPI 명령-데이터 시퀀스**:
   - `CS LOW` -> `Opcode(명령어)` 전송 -> `Address(주소)` 전송 -> `Data 송수신` -> `CS HIGH`
2. **W25Q64 Flash 통신 명령어 분석**:
   - `0x9F`: JEDEC ID 읽기 (제조사 및 장치 ID)
   - `0x06`: Write Enable
   - `0x03`: Read Data
   - `0x02`: Page Program (256B 쓰기)
   - `0x20`: Sector Erase (4KB 지우기)
3. 고속 DMA SPI 전송을 통한 LCD 화면 버퍼 갱신 원리
