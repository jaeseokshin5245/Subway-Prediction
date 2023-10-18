
# 📛 도착시간과 혼잡도를 고려한 대전 지하철 출발 시간 예측 / Daejeon Subway Departure Time Prediction Considering Arrival Time & Congestion
경사하강법을 활용한 대전 지하철 출발 시간 예측.  
This is a Prediction of Daejeon Subway Departure Time using Gradient Descent 

## 🧾 프로젝트 소개 / Project Description
대전 지하철 승하차 데이터셋을 경사하강법을 사용해 소요시간과 혼잡도을 고려한 목적지 역 도착을 위한 열차 출발 시각 알림.

기존에는 각 역별 시간표와 지도 어플리케이션이 제공하는 가장 가까운 지하철까지의 남은 도착 시간 알림만 제공. 

또한, 서울에 비해 대전은 각 차량별 혼잡도가 역 내 또는 지도 어플리케이션에서 제공되지 않고 있음.

따라서, 목적지역까지의 소요시간과 혼잡도를 고려해 출발역에서의 적절한 탑승 시각을 알게 함

다만, 학습 데이터의 한계, 천재지변이나 교통량에 따른 승하차 인원의 변동으로 값이 부정확해질 수 있음.

This is a notification program which informs subway department times considering lead time and congestion to arrvie destination station with gradient descent method using Daejeon subway dataset

Currently, we could get timetable of the each station and remaining time of incoming subway from the mobile map application.

So, This will let user know the getting on time considering cogestion and lead time to the destination station from the departure station.

But, due to the limitation of the dataset, delay or cancel by natural factors might make consequences incorrect.

### ⏲️ 개발 기간 / Develop Period
+ 2023년 4월 6일 ~ 2023년 6월 8일 (약 2개월)  
April 6th, 2023 ~ June 8th, 2023 (nearly 2 months)

### 🖥️ 개발 환경 / Built with

#### 사용 언어 / Language

+ 파이썬 / Python 

#### 프로그래밍 환경 / Programming Enviornment
+ 주피터 노트북 : 각 함수별 계산 결과를 보기 위해 사용.  
Jupyter Notebook : To see the result of functions seperately.  

+ 비주얼 스튜디오 코드 : 개발을 위한 통합 개발 환경으로 사용.  
Visual Studio Code : Used as IDE for development.
  
#### AI model
+ 경사하강법: 최적 출발 시각 계산을 위한 함수로 사용.  
Gradient Descent Method : Used as function to calculate the optimal departure time.

### 📤 버전별 업데이트 / Versioning

+ 0.1.0 : 최초 업데이트 Initial Update (2023-07-23)

## 🔌 프로젝트 설치 /  Installation
### 🏗️ 필요 조건 및 환경 / Prerequisites & Enviornment
+ Numpy
+ Matplotlib
+ Pandas
+ Jupyter Notebook

## 🏁 프로젝트 실행 / Project Execution
### 📣 실행 시작 / Start Execution 
#### ipynb 파일 실행 시 / Running ipynb file
1. aaaa
2. bbbb
3. cccc
4. ddddd
5. eeee
#### py 파일 실행 시 / Running py file
### 🔍 프로젝트 기능 / Function of Project
#### 출발 시각 예측 / Prediction of the departure time

#### 혼잡도 추정 / Estimation of the Congestion

## 📝 테스트 과정 및 결과 / Running Test & Result
### 🏕️ 테스트 환경 / Test Enviornment
+ Window 10 64bit OS
+ RAM 16GB
+ Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz

#### ⛰️ 테스트 실행 환경 / Test Execution Enviornment
+ Numpy : v1.23.5
+ Matplotlib : v3.7.1
+ Pandas : v2.0.0
+ Python : v3.11.0
+ VS Code : v1.83.0

#### 📌 (하이퍼) 파라미터 설정 / (Hyper) Parameter Setting

+ 학습 횟수 Epoch : 800

+ 학습률 Learning Rate : 5e-4 (0.005)

### 📐 테스트 평가 지표 / Index of test Evaluation 

## 📎 참고 및 사용 자료 / References
## 💳 라이센스 / License
## 🙇 후기 / Acknowledgment
