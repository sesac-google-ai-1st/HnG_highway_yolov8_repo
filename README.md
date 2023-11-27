# HnG_highway_yolov8_repo

> 고속도로 CCTV 영상 데이터를 활용한 차량 인식 프로젝트

![project image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/f84abe72-dc01-4aa1-ba52-0f861b864cc1)


600개의 background image를 추가하고 xl 모델을 사용하여 best.pt를 구한 결과입니다.
![result image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/72022988/b2ea1fdd-cd31-4bb2-985a-8da2b06fc050)




# Contents

[1. 프로젝트 소개](#1-프로젝트-소개) <br>
[2. 데이터](#2-데이터) <br>
[3. 실험](#3-실험) <br>
[4. 결과](#4-결과) <br>
[5. 활용 방안](#5-활용-방안) <br>
[6. 프로젝트 회고](#6-프로젝트-회고) <br>



# 1. 프로젝트 소개

### 목표

- "고속도로 CCTV 교통 영상" 데이터를 활용하여 YOLOv8로 Vehicle Object detection

- 평가기준 : mAP50-95

### 수행 기간 및 팀원

- 🗓️ 수행 기간 : 2023.11.20 ~ 24 (5일)

- 👥 팀원 (2명)<br>

    |박영현|최지민|
    |:-:|:-:|
    |<img src='https://avatars.githubusercontent.com/u/72022988?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/97524127?v=4' height=80 width=80px></img>|
    |[Github](https://github.com/yhp2205)|[Github](https://github.com/timmyeos)|

### 모델 학습 환경

- **GCP** (Google Cloud Platform)

    ![env](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/72022988/2a8c8554-13f3-491f-b38e-655656a1d5dc)


# 2. 데이터

- AI Hub의 [교통문제 해결을 위한 CCTV 교통 영상(고속도로)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=164)
  
    [![image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/266be1c4-8979-4f71-a610-3f7da727c4da)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=164)

- 바운딩박스 > 수도권 영동선의 CH01 ~ CH04 만 사용
- 데이터 용량 , 개수, 분포 등등


# 3. 실험

 - baseline
   - model: YOLOv8 nano
   - epochs: 25
   - batch: 128
   - imgsz: 640
   
    ~결과사진~


# 4. 결과

# 5. 활용 방안

# 6. 프로젝트 회고

