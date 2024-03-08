import pandas as pd

url="https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="
years = range(2020, 2023)

df = pd.DataFrame([])
for i in years: 
  df1 = pd.read_html(url+str(i))[0]
  df1["년도"] = str(i)
  df = pd.concat([df, df1])

df = df.replace({"kt":"KT", "SK":"SSG", "넥센":"키움"})  # 팀명이 바뀐팀들 팀명 수정

print("=" * 100)
print(df.pivot(values="순위", index="년도", columns="팀"))
print("=" * 100)
print(df.pivot(values="팀", index="년도", columns="순위"))