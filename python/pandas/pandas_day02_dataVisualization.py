# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WzDBvBYcQFKEt6YDqN7libURH03-Nsnk
"""

pip install xlrd==1.2.0

import pandas as pd

pd.read_excel('./seoul.xls', header=1, usecols='C:K')

col_names = ['스트레스', '스트레스남학생', '스트레스여학생', '우울감경험률','우울남학생','우울여학생', '자살생각율','자살남학생','자살여학생']
pd.read_excel('./seoul.xls', header=1, usecols='C:K', names=col_names)
raw_data = pd.read_excel('./seoul.xls', header=1, usecols='C:K', names=col_names)
raw_data

raw_data.loc[1] = 100-raw_data.loc[0]
raw_data

raw_data['응답'] = ['그렇다','아니다']
raw_data
raw_data2 = raw_data.set_index('응답')
raw_data2

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

raw_data2

import matplotlib.pyplot as plt

plt.rc('font', family='NanumBarunGothic')

raw_data2['스트레스'].plot.pie(explode=[0,0.02]) #explode=[0,0.02] : 그래프의 간격이 떨어짐

#차트 3개 동시에 띄우기
f, ax = plt.subplots(1,3,figsize=(16,8)) #f: 전체 표를 의미 ax: 축 / 1행 3열

#1번째축
raw_data2['스트레스'].plot.pie(explode=[0,0.02], ax=ax[0], autopct='%1.lf')
ax[0].set_title('스트레스를 받은적 있다.')

#2번째축
raw_data2['우울감경험률'].plot.pie(explode=[0,0.02], ax=ax[1], autopct='%1.lf')
ax[1].set_title('우울증을 경험한적 있다.')

#3번째축
raw_data2['자살생각율'].plot.pie(explode=[0,0.02], ax=ax[2], autopct='%1.lf')
ax[2].set_title('자살을 고민한적 있다.')

#데이터를 저장하기

#데이터프레임 만들기
#1. [[]] 2.df 3. 딕셔너리이용
#딕셔너리를 이용해 데이터프레임 생성
practice = pd.DataFrame({
    '날짜':[],
    '운동':[],
    '양':[]
}) 
practice

#날짜, 운동, 양
practice.loc[0] = ['19-03-01', '달리기', 1.]
practice.loc[1] = ['19-03-02', '걷기', 1.]
practice.loc[2] = ['19-03-02', '달리기', 1.]
practice.loc[3] = ['19-03-02', '계단오르기', 1.]
practice

practice.loc[4] = ['19-03-03', '걷기', 1.5]
practice.loc[5] = ['19-03-03', '달리기', 1.]
practice

practice.to_csv("./practice.csv", encoding='utf-8')

#엑셀 불러오기
pd.read_csv("./practice.csv", encoding='utf-8', index_col=0)

practice.loc[6] = ['19-03-04', '걷기', 1.5]
practice.loc[7] = ['19-03-05', '달리기', 1]
practice.loc[8] = ['19-03-06', '걷기', 2.5]
practice.loc[9] = ['19-03-06', '달리기', 0.5]
practice

#pivot_table
practice.pivot_table(index='운동', aggfunc="sum") #index와 columns는 이름 중복불가, aggfunc:average(default)
#테이블 합치거나 연산을 할 때, 수치데이터만... 수치로 나타낼수 없는 건 무시함

practice.pivot_table(index='운동', aggfunc=["sum", len])

#pivot(index, columns, values)로 테이블 변형 가능하다.
prac_pivot = practice.pivot('날짜','운동','양')
prac_pivot

prac_pivot = prac_pivot.fillna(0)#NaN 0으로 바꾸는법
prac_pivot

prac_pivot = practice.pivot('운동','날짜','양')
prac_pivot

#오늘의 마지막 예제,,
df = pd.read_excel("./exercise.xls")
df

df.head(5) #꼬리 df.tail(5)
#df = df.drop(columns='기간')
#df = df.drop(index=range(22,53))
#df = df['대분류'] == '성별'

