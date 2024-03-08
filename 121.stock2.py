import FinanceDataReader as fdr
import pandas as pd
df_krx = fdr.StockListing('KRX').iloc[:, :3]
stocks = ["005930", "035720"] #stocks를 바꾸면 수집하는 종목이 바뀜
df1 = pd.DataFrame()
for i in stocks:
    df = fdr.DataReader(i, '2018-06-30', "2018-07-30") # 날짜를 바꾸면 수집하는 기간이 바뀜
    df["Code"] = i
    df1 = pd.concat([df1, df])
df1.reset_index().merge(df_krx, how="left")