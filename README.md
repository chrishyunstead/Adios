# Adios팀 프로젝트
![image](https://github.com/Kshi0219/Adios/assets/149676714/0505755b-91f5-4f97-a42b-860c0aadd829)
-----
#### 1.주제
- __부산항 입항 외국인 선원 대상 마케팅 인사이트 제공__
    - 선용품 구매플랫폼 구축을 위한 데이터 분석 및 시각화
    - 외국인 선원 체류 시간별 관광코스 정보 제공

#### 2/프로젝트 기간
- 2024/02/27 ~ 03/05

#### 3.R&R(Role and Responsibility)
- __김동휘__ : 기획, 데이터 수집, 데이터 가공, 시각화(워드클라우드, Osmnx), 상관분석, Git관리
- __임경란__ : 데이터 수집, 데이터 가공, 시각화(워드클라우드, 공실데이터, Osmnx), 발표PPT 제작
- __정현수__ : 데이터 수집, 데이터 가공, 시각화(워드클라우드, 공실데이터), 상관분석
- __김성일__ : 데이터 수집, 데이터 가공, 시각화(워드클라우드, 공실데이터), 상관분석, Streamlit 배포
- __신대근__ : 데이터 수집, 데이터 가공, 시각화(워드클라우드, Osmnx), 상관분석

#### 4.사용 언어 및 라이브러리
- __언어__ : Python
- __라이브러리__
    - Pandas, Numpy, Prophet, Networkx, Scikit-learn, Scipy, Selenium, Beautifulsoup, matplotlib, Plotly, Osmnx, Folium, Googlemaps, Streamlit
    - 기타 시각화 툴 : Flourish
-----
#### 4.코드컨벤션
* __변수, 함수, 인스턴스 작성시 카멜케이스 명명 규칙을 따른다__
    * ex) camelCase
* __함수명 작성시 동사 + 명사 규칙을 따른다__
    * ex) getValue()
* __변수명 작성시 명사형태로 명명한다__
    * 변수이름은 짧지만 의미가 있어야 한다
    * 변수명만 봐도 사용한 이유를 알 수 있게 지어야 한다
    * 합성어 두개 이상일시 연결 기호는 _ 로 통일한다
* __Str 형식 또는 파일명 불러올시 기본 “ ”, ‘’’ ‘’’을 사용한다__
* __코드에는 주석을 반드시 기재한다__
    * 코드설명, 사용이유 등
* __rawData를 불러올시 주석으로 최소한의 MetaData를 기재한다__
    * ex) 자료출처, 파일형식, 핵심필드 및 데이터 타입
* __파이썬 파일 명명은 영문으로 기재하며 과업_데이터.ipynb 로 지정한다__
    * ex) pretreatment_ShipSupplies, Visualization_ShipSupplies
* __파이썬 파일 명명은 영문으로 기재하며 과업_데이터.파일형식 로 지정한다__
    * ex) pretreatment_ShipSupplies, Visualization_ShipSupplies, 로우데이터일시 Raw_ 앞에 붙여서 기재
* __파일형식은  ipynb 으로 저장한다__
* __rawData와 가공 Data 는  각 Before 또는 After 디렉토리에 저장한다__
-----
#### 5.산출물
##### (1) 스트림릿 앱
* 링크 :https://busanportservice.streamlit.app/
##### (2) giHub
* https://busanportservice.streamlit.app/

-----
#### Udate Log
* Deploy_date : 2024/03/05
