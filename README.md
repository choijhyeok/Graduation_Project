# AI를 활용한 안면인식 출결시스템

&nbsp;

## 1. 목적 및 동기

 - 코로나 상황에서 zoom으로 비대면 수업 때문에 교수님이 출석을 부르면서 시간이 지체됨
 - 비대면 수업으로 인해 대리출석의 위험성이 커지고 있는 상황

:rocket: 이를 해결하기 위해서 안면인식 출결 시스템을 고안

&nbsp;

## 2. 전체 흐름도

![flowchart](http://drive.google.com/uc?export=view&id=16Hxw2sNN7lVth2Qml6s-JSGDXRLYVhTU)



&nbsp;
## 3. 필수 설치 패키지

requirements.txt의 패키지를 설치해야 함

```
appdirs==1.4.3
attrs==19.1.0
black==19.3b0
Click==7.0
cycler==0.10.0
demjson==2.2.4
kiwisolver==1.1.0 
matplotlib==3.1.1
nose==1.3.7
numpy==1.17.0
opencv-contrib-python==4.1.0.25
pandas==0.25.1
Pillow==6.2.0
pyparsing==2.4.2
python-dateutil==2.8.0
pytz==2019.2
six==1.12.0
toml==0.10.0
virtualenv==16.7.4
xlrd==1.2.0
xmltodict==0.12.0
yagmail==0.11.220
yapf==0.28.0
Flask==1.1.2
```

## 4. 실행방법

종속 패키지를 모두 설치 후에 flask_app.py 을 실행

```
python flask_app.py

# 나온 ip로 접속
```

## 5. 회원가입, 로그인 안면인식 화면

- 회원가입시 Capture_Image.py 에서 120초간 사진 캡쳐 후 저장 , 저장된 이미지 Train_Image.py 통해서 재학습

![train](http://drive.google.com/uc?export=view&id=1h54xdajPeVdeaVtGjr0jP1USQb5VYDvo)

&nbsp;
- 로그인시 Recognize.py 에서 일치율 확인 일치율 68% 이상일시 통과

![check](http://drive.google.com/uc?export=view&id=1N3xWN146txTRzHpZD050VpKnikoNRrrM)
