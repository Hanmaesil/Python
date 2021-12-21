#!/usr/bin/env python
# coding: utf-8

# # 파이썬

# In[1]:


#주석처리


# In[2]:


1+3 #1더하기3 실행


# In[3]:


print(5)


# In[4]:


10*21


# In[5]:


print("Hello World!!")


# In[6]:


print('Hello World!!!')


# In[7]:


print(5<10)


# In[8]:


print(5>10)


# In[9]:


num = 3
print(num)


# In[10]:


num1 = 13
num2 = 25
num3 = 77
print(num1)
print(num2)
print(num3)


# In[11]:


a = 10
b = 15
print(a,b)


# In[12]:


a, b = 10, 15
print(a)
print(b)
print(a,b)


# In[13]:


#str1 에 python 대입, str2 에 python 대입
str1 = str2 = "python"
print(str1, str2)


# In[14]:


#변수 x에는 100을 대입, 변수 y에는 200을 대입후 변수 sum에는 두변수의 합을 대입하여 출력
x = 100
y = 200
sum = x+y
print(sum)


# In[15]:


"she's gone"
str = "She's gone"
print(str)
s = 'She\'s gone'
print(s)


# In[16]:


#개행 실습
s1 = "자세히 보아야 이쁘다.\n오래 보아야 사랑스럽다.\n너도 그렇다."
print(s1)
s2 = """자세히 보아야 이쁘다.
오래 보아야 사랑스럽다.
너도 그렇다."""   #싱글로 3개해도 된다. ->> \n 또는 """문자열""" 또는 '''문자열'''
print(s2)


# # 인덱싱

# In[17]:


#인덱싱
name = "My name is GI"  #자바의 배열과 같이 0부터 시작한다, 띄어쓰기 칸도 포함하여 카운팅한다.
print(name[3])
#i를 가져오기
print(name[8])
print(name[-5])   #배열의 끝부터 가져오고 싶을때는 -1부터 시작한다.


# # 슬라이싱

# In[18]:


#슬라이싱
print(name[11:13])  # 가져오고 싶은 인덱스의 이상, 미만(마지막 숫자를 1크게 한다.)
#name가져오기
print(name[3:7])
print(name[-10 : -6])
#전체 문자열 가져오기
print(name)
print(name[:]) #인덱스 번호를 적지 않으면 끝과 끝으로 인식하여 전부 출력된다.
print(name[11:]) #번호를 적지않으면 끝으로 인식하여 출력된다.
print(name[-2 :]) # '-' 사용시 출력
print(name[-2:]) 
print(name[1: -7])  #섞어서 사용할 때 순서를 주의할 것.
print(name[3] + name[5])
print(name[3],name[5]) #순서대로 불러오는 것이기 때문에 띄어쓰기가 들어간다.


# In[19]:


#문자열 출력
day = "2021년 12월 21일의 날씨는 추움입니다."
#날짜 : 2021년 12월 21일 
#날씨  : 맑음 
print("날짜 : " + day[0:13])
print("날짜 :",day[0:13])
print("날짜 :",day[:13])

print("날씨 : " + day[19 : 21])
print("날씨 :",day[19 : 21])


# In[20]:


# s3 = 2021+'년'


# # 문자열 포맷팅!

# In[ ]:


#오늘은 12월 21일 입니다.
day = 21
s = "오늘은 12월 %d일 입니다."%day #정수형
day = "21"
s = "오늘은 12월 %s일 입니다."%day #문자형
print(s)


# In[ ]:


s = '오늘은 12월 {}일 입니다.'.format(day)
print(s)


# In[ ]:


s = f"오늘은 12월 {day}일 입니다."
print(s)


# In[ ]:


#실습 
#변수 x에는 100을 대입, 변수 y에는 200을 대입후 변수 sum에는 두변수의 합을 대입하여 출력(100와 200의 합은 300입니다 로 출력)

x = 100
y = 200
sum2 = x+y
print("%d와 %d의 합은 %d입니다."%(x,y,sum2))
print(f"{x}와 {y}의 합은 {sum2}입니다")
print("{}와 {}의 합은 {}입니다.".format(x,y,sum2))


# # 문자열 포맷코드

# ![image.png](attachment:image.png)

# # 산술 연산자

# In[ ]:


num1 = 10
num2 = 7
#나누기, 나머지, 몫 구하기
print(num1 / num2) #나누기
print(num1 // num2) # 몫
print(num1 % num2) # 나머지


# In[ ]:


print(num1 + num2)


# In[3]:


str1 = "안녕"
str2 = "하세요"
str3 = "10"
str4 = "7"
num3 = 7
print(str1 + str2)
print(str3 + str4)
# print(str3 + num3) #자료형이 달라서 연산이 안된다
print(int(str3) + num3)
print(str3 + str(num3))


# In[1]:


str1 = "10"
num3 = 8
print(str1+str(num3))


# In[19]:


num1 = 23
num2 = 3
print(f"더하기 결과 : {num1 + num2}")
print(f"빼기 결과 : {num1 - num2}")
print(f"곱하기 결과 : {num1 * num2}")
print(f"나누기 결과 : {num1 / num2}")

print()
print("더하기 결과 : %d"%(num1+num2))


# # 키보드로 입력 받아서 연산 진행

# ## input()함수 사용

# In[20]:


name = input()


# In[21]:


print(name)


# In[28]:


num = int(input("정수를 입력하세요 >>>"))  #기본형은 문자열로 된다.
print(num)


# In[29]:


type(num) #자료형을 알려준다.


# In[32]:


num1 = int(input("첫번째 정수를 입력하세요 >> "))
num2 = int(input("두번째 정수를 입력하세요 >> "))

print(f"더하기 결과 : {num1 + num2}")
print(f"빼기 결과 : {num1 - num2}")
print(f"곱하기 결과 : {num1 * num2}")
print(f"나누기 결과 : {num1 / num2}")


# In[46]:


# num1, num2 = int(input("정수입력 >>"))   어떻게 안되나...?ㅠㅠ
# print(num1)
# print(num2)
# print(num1+num2)


# In[3]:


#실습
python = int(input("python 점수 입력 >>"))
ml = int(input("머신러닝 점수 입력 >>"))
dl = int(input("딥러닝 점수 입력 >>"))
sum = python + ml + dl
avg = sum/3
print(f"합계 : {python + ml + dl}")
print(f"평균 : {(python + ml + dl)//3}")

print()

print("합계 : %d"%sum)
print("평균 : %d"%avg)

print()

print("합계 : {}".format(sum))
print("평균 : {}".format(avg))


# # 지수연산자(**)

# In[4]:


num = 3
power = 2
print(num ** power)


# # 대입연산자

# In[ ]:


#자바랑 똑같다.


# # 치환

# In[8]:


a = 3
b = 7


# In[11]:


#자바에서 했던 치환 방식
temp = a
a = b
b = temp
print(a)
print(b)


# In[12]:


#파이썬에서의 치환
a, b = b, a
print(a)
print(b)


# # 비교연산자

# In[ ]:


#자바랑 같다!


# # 논리연산자

# In[14]:


# not, and, or


# In[17]:


a = 1
b = 5
print(a < b)
not a < b


# In[18]:


# 프린터문 안에 넣지 않으면 마지막 것만 출력된다
print(a)
a
b

