# HnG_highway_yolov8_repo

> 고속도로 CCTV 영상 데이터를 활용한 차량 인식 프로젝트

![project image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/f84abe72-dc01-4aa1-ba52-0f861b864cc1)


# 🚗🚌🚛 Demo 

![demo_croped](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/a9acd260-eeb5-49bb-9e73-9919b218b86e)


## 🤗 Best model validation result
![result image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/df01591a-786f-42e0-950e-05ed347845ed)

## How to run
```python
!git clone https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo.git
%cd HnG_highway_yolov8_repo
!pip install -r requirements.txt

# models dir 하위 모든 모델로 변경 가능
model_path = "./models/train_back_x100/weights/best.pt"
# test를 원하는 이미지/동영상 경로
test_src_path = "test_image.png"

!yolo task=detect mode=predict model={model_path} conf=0.25 source={test_src_path}
```

---

<br>

# 📃 Contents

[1. 프로젝트 소개](#1-프로젝트-소개) <br>
  - [목표](#목표)
  - [수행 기간 및 팀원](#수행-기간-및-팀원)
  - [repo structure](#repo-structure)
  - [모델 학습 환경](#모델-학습-환경)
  - [Project Workflow]()
  
[2. 데이터](#2-데이터) <br>
  - [EDA 요약](#eda-요약)

[3. 실험](#3-실험) <br>
  - [baseline](#0-baseline)
  - [실험 1 : model size & epoch up](#실험-1--model-size--epoch-up)
  - [실험 2 : class imbalance](#실험-2--class-imbalance)
  - [실험 3 : add background data](#실험-3--add-background-data)

[4. 결과](#4-결과) <br>

[5. 프로젝트 회고](#5-프로젝트-회고) <br>
  - [어려웠던 점](#어려웠던-점)
  - [배운 점](#배운-점)


<br>

# 1. 프로젝트 소개

### 목표

- "고속도로 CCTV 교통 영상" 데이터를 활용하여 YOLOv8로 Vehicle Object detection
  - COCO dataset으로 pretrained 된 [YOLOv8](https://docs.ultralytics.com/models/yolov8/) 모델을 <br> AI Hub "고속도로 CCTV 교통 영상" 데이터셋으로 fine tuning

- 객체 검출 정확도 평가 metric : **mAP50-95**
    - IoU (Intersection over Union = $\frac{교집합}{합집합}$) : 정답과 예측값의 바운딩 박스가 얼마나 겹치는가를 0 ~ 1 사이의 값으로 나타낸 것 <br>
    - Precision (= $\frac{TP}{TP+FP}$) : 검출된 결과들 중 옳게 검출한 비율
    - Recall (= $\frac{TP}{TP+FN}$) : 검출해야하는 결과를 얼마나 검출했는지의 비율
    - Precision-Recall Curve : confidence level에 따른 Precision과 Recall값의 변화 곡선
      - IoU에 따라 TP와 FP를 결정
      - confidence level에 따라 검출된 바운딩 박스의 유효 개수가 변함
    - AP : 
    - mAP : 객체 종류별(car, bus, truck) AP의 평균값
    - mAP50-95 : IoU 0.5부터 0.95까지 0.05 간격으로 mAP값을 구해서 평균한 값

### 수행 기간 및 팀원

- 🗓️ 수행 기간 : 2023.11.20 ~ 24 (5일)

- 🤲 팀원 (2명)<br>

    |박영현|최지민|
    |:-:|:-:|
    |<img src='https://avatars.githubusercontent.com/u/72022988?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/97524127?v=4' height=80 width=80px></img>|
    |[Github](https://github.com/yhp2205)|[Github](https://github.com/timmyeos)|

### repo structure

```python
├── README.md
├── requirements.txt
├── test_image.png
├── code
│  ├─ EDA
│  │   ├─ highway_EDA.ipynb
│  │   ├─ highway_train.csv
│  │   └─ highway_valid.csv
│  ├─ data_handling
│  │   ├─ draw_bounding_box.py
│  │   ├─ highway_dataset_preprocess.ipynb
│  │   ├─ highway_images_folder_merge.ipynb
│  │   └─ highway_labels_xml2txt.ipynb
│  └─ train.ipynb    # YOLOv8 모델 학습
└── models    # 각 모델 폴더 하위 weights 폴더에 pt 파일 있음 
   ├─ train_aug_m71
   ├─ train_back_m100
   ├─ train_back_x100   # best model
   ├─ train_de_m100
   ├─ train_m100
   ├─ train_m400
   ├─ train_n25   # baseline
   └─ val_back_x100
```

### 모델 학습 환경

- ultralytics 버전 :  8.0.20
- **GCP** (Google Cloud Platform)

    ![env](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/72022988/2a8c8554-13f3-491f-b38e-655656a1d5dc)

### Project Workflow
![workflow](https://github.com/sesac-google-ai-1st/saramin-repo-1/assets/97524127/129bf398-3ade-445d-adaf-7a6fb027859e)


# 2. 데이터

### AI Hub [교통문제 해결을 위한 CCTV 교통 영상(고속도로)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=164) > 바운딩박스 > 수도권 영동선의 CH01 ~ CH04 사용
  
[![image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/266be1c4-8979-4f71-a610-3f7da727c4da)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=164)

- 데이터 용량

  ![스크린샷 2023-11-30 132142](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/72022988/20f5cc82-da2d-47a6-88e6-2c9bee1968c4)

- 최종 데이터 구조
  ```
  dataset
  ├─ train
  │ ├─ images
  │ └─ labels
  ├─ validation
  │ ├─ images
  │ └─ labels
  └─ data.yaml
  ```

- 데이터 개수
  - train 총 데이터 개수: 23951
  - valid 총 데이터 개수: 3333

### EDA 요약
- image 파일 이름과 label을 통해 추출한 정보
 
  <img src='https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/72022988/16805727-3d8d-417b-a94a-87cd163d14a5' width="700" height="200" />  

- image 데이터의 시간 및 날씨 분포 (train , valid)
  | 시간 | 날씨 |
  |:----:|:----:|
  | ![time image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/6fedd5d0-e99e-4919-9d8d-9da87c04ff17) | ![weather image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/1b4e370b-868b-43e6-9e56-1eb2a10d2c12) |
- label 분포 : car >>>>> truck > bus
  
  <img src='https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/8671432a-a27c-4015-8184-a9c5aff87cbb' width="450" height="350" />

➜ **train과 valid의 데이터가 매우 유사한 것을 확인함**

<br>

# 3. 실험

## 0. baseline

|   name   | YOLOv8 model | epoch | batch | imgsz | metric (mAP50-95) |
|:--------:|:------------:|:-----:|:-----:|:-----:|:-----------------:|
| baseline |     nano     |   25  |  128  |  640  |       0.743       |

![baseline result](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/bf3b3450-b348-40e4-847a-008094830b8d)

![result png image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/475e47df-1d4a-4254-a731-b1cd5bd5a06e)
![confusion matrix image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/d37416d6-a2f1-4163-8aa2-ae462a4c82d2)


![mind map](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/2246ce5c-a487-4602-a584-eb01f3f26c2f)




## 실험 1 : model size & epoch up

|   name   | note | YOLOv8 model | epoch | batch | imgsz | metric (mAP50-95) |
|:--:|:--------:|:------------:|:-----:|:-----:|:-----:|:-----------------:|
| baseline |  |    nano     |   25  |  128  |  640  |       0.743       |
| **exp1** | model & epoch ↑ <br> EarlyStop|    medium     |   58  |  92<sup>[1](#footnote_1)</sup>  |  800  |       **0.813**       |

<a name="footnote_1">1.</a> GPU 4개를 사용하였는데, `batch=128` 로 설정 시 `Out Of Memory 에러` 발생. 128보다 작으면서 4의 배수인 92로 설정함.

![m400](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/2afa5d30-5f7a-4ec2-a452-d73f12d9aa03)

### ➜ exp1 실험 결과
  - 모델 사이즈를 nano에서 medium model로 키우고, 학습 epoch를 25에서 58로 늘린 결과,<br> mAP50-95가 0.743에서 0.813로 0.07만큼 **상승**했음

<br>

## 실험 2 : class imbalance

![add data image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/79c71535-a439-45d3-91cd-47bd9ab81b88)

- 데이터를 추가함
  - 기존 : validation data로 CH01 ~ CH04만 쓰기 때문에, train data도 CH01 ~ CH04만 사용하였음
  - 실험2 : 기존에 train에 사용하지 않은 CH05 ~ CH10의 데이터를 추가
    - 실험1로 mAP50-95가 상승하였기 때문에, 실험1에 기반하여 YOLOv8 model medium으로 함
    - bus와 truck을 위주로 추가하고자 함
    - (bus + truck) 개수가 car의 개수 보다 많은 이미지만 선택 : 3268장<br>
      `train_df[train_df['car']<=(train_df['bus']+train_df['truck'])]` <br>

|   name   | note | YOLOv8 model | epoch | batch | imgsz | metric (mAP50-95) |
|:--:|:--------:|:------------:|:-----:|:-----:|:-----:|:-----------------:|
| baseline |  |    nano     |   25  |  128  |  640  |       0.743       |
| exp1 | model & epoch ↑ <br> EarlyStop |    medium     |   58  |  92  |  800  |       **0.813**       |
| **exp2** | class imbalance <br> 시간관계상 Stop |    medium     |   68  |  64  |  640  |       **0.806**       |


![aug m71](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/b182c20f-ceaf-4991-8ece-9dd459059d02)

### ➜ exp2 실험 결과
-  기존 train에 사용하지 않은 CH05 ~ CH10의 데이터를 추가한 exp2의 mAP50-95는 0.806로, exp1 보다  0.007만큼 낮음
     - validation 이미지는 CH01 ~ CH04의 이미지뿐이라서, 오히려 그 외 채널 이미지를 학습한 것이 평가에 방해됐나?
     - exp1 보다 imgsz가 낮아서?
     - 더 학습을 하면 성능이 올라갈 수 있었는데, 시간 관계 상 멈춰서?

<br>

## 실험 3 : add background data


- background 데이터를 추가함
  [![스크린샷 2024-01-08 093531](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/09d24cdc-af57-4362-bd10-e55857db202f)](https://its.go.kr/map/cctv)

  - 고속도로 CCTV 자료를 제공하는 [국가교통정보센터](https://its.go.kr/map/cctv)에서 차가 없는 빈 도로 (background) 이미지 150장을 캡쳐함
  - 위 사이트에서 캡쳐한 이미지를 augmentation(Resize, Crop, Cropout 등) 하여 599장으로 데이터 증강
  - `train/images` 에 증강한 background 이미지 **599장** 추가<br>
      background 이미지 추가 방법: https://github.com/ultralytics/yolov5/issues/2844

  <img width="290" alt="background image 1" src="https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/72022988/816d0ad6-2c10-4894-8478-1119557064d6"> <img width="300" alt="background image 1" src="https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/72022988/a6e1fdd5-9e0c-43ec-8940-b9eccd0a3018">

  <br/>
|   name   | note | YOLOv8 model | epoch | batch | imgsz | metric (mAP50-95) |
|:--:|:--------:|:------------:|:-----:|:-----:|:-----:|:-----------------:|
| baseline |  |    nano     |   25  |  128  |  640  |       0.743       |
| exp1 | model & epoch ↑ <br> EarlyStop |    medium     |   58  |  92  |  800  |       **0.813**       |
| exp2 | class imbalance <br> 시간관계상 Stop |    medium     |   68  |  64  |  640  |       0.806       |
| **exp3-1** | background <br> EarlyStop |    medium     |   40  |  92  |  800  |       **0.814**       |
<br/>

![back m100](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/f6269eb7-130d-473a-a119-bffbe689613b)

### ➜ exp3-1 실험 결과
  - exp3-1은 기존에 가장 높은 성능을 보인 exp1과 동일한 세팅에 background 이미지를 추가한 것
  - exp1과 exp3-1는 background 이미지 차이뿐인데, 거의 모든 성능 지표에서 exp3-1가 미세하게 높음
    - 상승한 지표
      - Precision: all은 0.909에서 0.917로 0.008만큼 상승, car는 0.94에서 0.942로 0.002만큼 상승, bus는 0.893에서 0.909로 0.016만큼 상승, truck은 0.893에서 0.9로 0.007만큼 상승
      - Recall: all은 0.884에서 0.886로 0.002만큼 상승, car는 0.92에서 0.921로 0.001만큼 상승, truck은 0.881에서 0.886로 0.005만큼 상승
      - mAP50: all은 0.943에서 0.947로 0.004만큼 상승, car는 0.973에서 0.974로 0.001만큼 상승, bus는 0.915에서 0.92로 0.005만큼 상승, truck은 0.942에서 0.946로 0.004만큼 상승
      - mAP50-95: **all은 0.813에서 0.814로 0.001만큼 상승**, bus는 0.785에서 0.786로 0.001만큼 상승, truck은 0.802에서 0.804로 0.002만큼 상승
    - 하락한 지표
      - Recall: bus가 0.852에서 0.851로 0.001만큼 하락
      - mAP50-95: car가 0.852에서 0.851로 0.001만큼 하락
  - **background 이미지 추가한 것이 효과 있다**는 의미
 
  <br/>

---
  <br/>

- 이전까지 실험한 결과, background 이미지를 추가한 exp3-1가 가장 높은 성능을 보였음
- 하지만 실험1을 통해 모델 사이즈를 키우면, 성능이 올라간다는 것을 확인했음
- exp3-2는 background 이미지를 추가한 exp3-1를 기반으로 하고, 실험1의 결과를 참고하여 모델사이즈를 medium에서 xlarge로 키움

|   name   | note | YOLOv8 model | epoch | batch | imgsz | metric (mAP50-95) |
|:--:|:--------:|:------------:|:-----:|:-----:|:-----:|:-----------------:|
| baseline |  |    nano     |   25  |  128  |  640  |       0.743       |
| exp1 | model & epoch ↑ <br> EarlyStop |    medium     |   58  |  92  |  800  |       0.813       |
| exp2 | class imbalance <br> 시간관계상 Stop |    medium     |   68  |  64  |  640  |       0.806       |
| exp3-1 | background <br> EarlyStop |    medium     |   40  |  92  |  800  |       0.814       |
| **exp3-2** | background <br> EarlyStop <br> **best model** |    **xlarge**     |   47  |  32  |  800  |       ✨ **0.823** ✨       |
  <br/>

![back x100](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/7ae50a8f-fb8b-4e64-8910-76d64e6f6ba0)
![results](https://github.com/sesac-google-ai-1st/3monkey_yolo/assets/97524127/b3b9d5e9-cbf6-413c-9f39-9082b004bf75)
![confusion_matrix_normalized](https://github.com/sesac-google-ai-1st/3monkey_yolo/assets/97524127/cee42e17-82fc-4102-98e6-de54e9befdcf)
### ➜ exp3-2 실험 결과
  
  - background 이미지를 추가한 exp3-1를 기반으로 하고, 모델 사이즈를 키우니,<br> **exp3-1의 mAP50-95는 0.814였는데, exp3-2는 0.823으로 0.09만큼 상승함**
  - 각 클래스(car, bus, truck)의 mAP50-95도 0.005~0.015만큼 상승하였음
  - 👏👏👏 best mAP50-95 결과를 얻음 👏👏👏
<br>

# 4. 결과

### baseline과 best model의 predict 비교<sup>[2](#footnote_2)</sup>
![highway-optimize](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/387caefc-53ff-48cb-b9fe-7e960dbaee12)

| baseline                                | best                               |
|:-----------------------------------------:|:------------------------------------:|
| CCTV 영상 내 글자("릉","동")를 car로 인식함        | 그런 현상 없음                     |
| 멀리서 오는 bus를 초반에 truck으로 인식 | 멀리서부터 bus로 인식              |

- **결론**
  - best model이 비교적 안정적으로 vehicle을 인식함
  - 데이터만 존재한다면 차 종을 인식하는 모델로 사용 가능
<br/>  

- **한계점**
  - 객체가 가로등이나 CCTV 내 글자에 가려지면 인식률이 떨어짐<sup>[3](#footnote_3)</sup>
  - 객체를 어느 정도 거리부터 인식할 수 있는지 기준이 정확하지 않음<sup>[4](#footnote_4)</sup>
  - 검증 영상의 화질에 따라 정확도에 영향을 미침
  - best 모델의 크기가 커서 검증 속도가 느리기 때문에 고속도로 실시간 분석에 어려움이 있음

<br>

<a name="footnote_2">2.</a> 영상 출처: [국가교통정보센터](https://its.go.kr/map/cctv) 영동선 신갈분기점 CCTV<br>
<a name="footnote_3">3.</a> 아래 사진에서 노란원을 보면, 가로등에 가린 차가 인식되지 않음.<br>
<a name="footnote_4">4.</a> 아래 사진에서 까만박스를 보면, 앞에 있는 car는 인식되지 않고, 그보다 뒤에 있는 truck을 인식한 것을 볼 수 있음.<br>
![image](https://github.com/sesac-google-ai-1st/HnG_highway_yolov8_repo/assets/97524127/4565cc3b-e529-48c4-bb22-fccf143013b8)


<br>


# 5. 프로젝트 회고

### 어려웠던 점
  - 모델 학습을 위해 데이터를 준비하는 과정
    - 데이터 용량이 너무 커서 (약 40GB) 데이터 다루는 데에 시간이 오래 걸림
      - AI Hub에서 데이터 다운받는 것
      - 압축한 zip 파일을 GCP cloud storage(bucket)에 업로드하는 것
      - bucket에서 zip 파일을 가져와서 압축 푸는 것 <br>
      ⇒  각각 n시간 소요됨
    - 이후에 빠른 방법을 찾아냄
      - AI Hub에서 데이터 다운 ➝ Workbench 터미널에서 바로 [AI Hub API](https://www.aihub.or.kr/devsport/apishell/list.do?currMenu=403&topMenu=100) 사용
      -  bucket에서 zip 파일 압축 푸는 것 ➝ multiprocessing을 통해 n초로 단축
  - Multi-GPU 사용
    - 학습 시, 한개의 GPU를 쓸 땐 문제가 없었는데 `device=[0,1]`을 설정하면 계속 에러 발생함
    - Troubleshooting
      - `pip install ultralytics` 시, 에러메세지 : `FileNotFoundError`
      - `git clone https://github.com/ultralytics/ultralytics`  시, 에러메세지 : `CalledProcessError` <br>
      ⇒ `pip`와 `git clone`을 둘 다 하니까 Multi-GPU 사용 가능했음
      - 프로젝트 수행 당시 ultralytics 버전(8.0.20)의 문제로 추측함

### 배운 점
  - GCP cloud storage(bucket)를 통해 대용량 데이터를 다루는 경험을 함
  - YOLO를 학습시키기 위한 custom dataset 구조를 알게 됨
  - 모델 성능 올리기가 쉽지 않았음
    - 여러 조건에서 실험을 진행했음에도 점수가 0.83 이상으로 높게 올라가지 않음
    - 시간이 충분했다면, 데이터를 더 적극적으로 수정/보완했을 것