
# Intelligent AI CCTV Analytics & Video Recorder

OpenCV와 딥러닝 모델인 YOLOv8x를 결합한 지능형 비디오 레코더 시스템입니다. 실시간 객체 인식, 객체 추적, 특정 영역 확대(ROI Zoom) 및 영상 녹화 기능을 제공합니다.

======사진: 메인 실행 화면 (YOLO 박스와 카운터가 보이는 화면)=======

## 주요 기능

### 1. 실시간 객체 인식 및 추적 (AI Analytics)

- YOLOv8x (X-Large) 모델을 활용하여 사람(Person) 및 차량(Car, Bus, Truck, Bike)을 실시간으로 식별합니다.
    
- 각 객체에 고유 ID를 부여하여 이동 경로를 추적(Tracking)하며, 화면 상단에 실시간 객체 수를 집계하여 표시합니다.
    

### 2. 고급 영상 녹화 시스템 (Advanced Recording)

- Record 모드 작동 시 실시간으로 경과 시간(REC 00:00)을 표시하며, 녹화 중임을 알리는 인디케이터가 깜빡입니다.
    
- AI 분석 결과와 사용자 필터가 적용된 화면 그대로 `.avi` 파일로 저장됩니다.
    

### 3. 인터랙션 및 영상 처리

- **Smart Zoom**: 마우스 좌클릭 드래그로 특정 영역을 지정하여 실시간으로 확대할 수 있습니다. (우클릭 시 해제)
    
- **Real-time Filters**: 명암비(Contrast), 밝기(Brightness) 조절 및 좌우 반전(Flip) 기능을 실시간으로 적용할 수 있습니다.
    

======사진: ROI 드래그 줌인 작동 화면=======


## 조작 가이드

- **Space**: 녹화 시작 및 중지 (REC 모드 전환)
    
- **ESC**: 프로그램 종료
    
- **f**: 화면 좌우 반전 (Flip)
    
- **= / -**: 영상 명암비(Contrast) 조절
    
- ] / [ : 영상 밝기(Brightness) 조절
    
- **마우스 좌클릭 드래그**: 특정 영역 확대 (Zoom-in)
    
- **마우스 우클릭**: 확대 해제 (Reset Zoom)
    

======사진 또는 영상: 실제 녹화된 결과물 파일의 스크린샷=======


## 시스템 사양 (System Requirements)

| **Component** | **Details**                                     |
| ------------- | ----------------------------------------------- |
| **CPU**       | AMD Ryzen 7600X                                 |
| **GPU**       | NVIDIA GeForce RTX 4070 Ti SUPER (16GB VRAM)    |
| **RAM**       | DDR5 48GB                                       |
| **CUDA**      | 12.7                                            |
| **Python**    | 3.11.9 (64-bit)                                 |
| **DL Model**  | YOLOv8x (X-Large) - SOTA Object Detection Model |
