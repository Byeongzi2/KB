#!/usr/bin/env python
# coding: utf-8

# # 효자동 인구 분포와 비슷한 동네 찾기

# <br/>
# <br/>
# <br/>
# <br/>

# ## 모듈 import

# In[1]:


import numpy as np
import pandas as pd
from IPython.display import display, HTML
display(HTML('<style>.container {width : 100%; !important;}</style>'))


# <br/>
# <br/>
# <br/>
# <br/>

# ## 데이터 로드

# In[2]:


# 202201_202201_연령별인구현황_월간.csv 파일을 읽으세요. (encoding = 'cp949', thousands = ',')
df = pd.read_csv("./202201_202201_연령별인구현황_월간.csv",
                 encoding = 'cp949',
                thousands = ",")
df


# <br/>
# <br/>
# <br/>
# <br/>

# ## 데이터 정보 조회

# In[3]:


# 행과 열의 개수를 구하세요.
df.shape


# In[7]:


# 컬럼명을 조회하세요.
df.columns


# In[9]:


# 세번째 컬럼 명 부터 슬라이싱하여 cols에 저장하세요. (인구 분포를 확인할 컬럼)
cols = df.columns[3:]
cols


# <br/>
# <br/>
# <br/>
# <br/>

# ## 데이터 타입 변경

# In[23]:


# 각 열 별 데이터 타입을 조회하세요.
df.dtypes


# <br/>
# <br/>
# <br/>
# <br/>

# ## 효자동과 사직동 인구 분포의 차이
# - 두 지역의 각 열 별 차이를 구한 뒤
# - 각 차이의 제곱의 합을 더한 값을 error라 정의한다.
# - 두 지역의 error가 작을수록 인구 분포가 비슷하다고 정의한다.

# In[34]:


# 2번 행(효자동 행), cols 컬럼을 선택하여 flag에 저장하세요.
flag = df.loc[2,:][3:]
flag


# In[35]:


# 3번 행(사직동 행), cols 컬럼을 선택하여 temp에 저장하세요.
temp = df.loc[3,:][3:]
temp


# In[36]:


# 두 지역의 각 열 별 차이를 구하세요.
flag-temp


# In[38]:


# 위 결과의 값에 제곱을 하세요.
error = (flag-temp)**2
error


# In[39]:


# 위 결과의 값을 모두 더하세요. (효자동과 사직동의 error)
error.sum()


# <br/>
# <br/>
# <br/>
# <br/>

# ## 효자동과 다른 동네의 인구 분포 차이
# - 위와 같은 방법으로 효자동을 기준으로 다른 동네와의 error를 구하여 result 리스트에 추가하세요.

# In[41]:


result = []

for i in range(len(df)) :
    # code here
    temp = df.loc[i,:][3:]
    error = (flag-temp)**2
    result.append(error.sum())

result


# In[43]:


# result 리스트를 pd.Series로 변환하세요.
result = pd.Series(result,dtype='float64')
result


# In[48]:


# 값을 기준으로 정렬하세요.
result.sort_values()


# In[49]:


# 3868 행을 조회하세요.
df.loc[3868]


# <br/>
# <br/>
# <br/>
# <br/>

# ## (참고) 시각화

# In[50]:


import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize = (16,6))

plt.plot(flag, label = '효자동')
plt.plot(df.loc[3868, cols], label = '중문동')
plt.legend()
plt.xticks([])
plt.show()

