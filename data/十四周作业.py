# %%
import pandas as pd
from scipy import stats
# 打开数据文件
file_path = R"C:\Users\LENOVO\Desktop\statistic\data\movie_data_cleaned.csv"
df_movies = pd.read_csv(file_path)


# %%
# 计算均值和标准误差
mean = df_movies['average'].mean()
std_error = stats.sem(df_movies['average'])
# 设定置信水平
confidence_level = 0.95
# 设定自由度
df = len(df_movies['average']) - 1
# 计算置信区间
confidence_interval = stats.t.interval(confidence_level, df, loc=mean, scale=std_error)
# 输出结果
print(F"均值：{mean: .2f}")
print(F"均值在置信水平{confidence_level}下的置信区间为：", confidence_interval)


# %%
# 使用sample函数实现随机抽取，并且计算出置信区间
import pandas as pd  
import random  
  
# 读取CSV文件  
data = pd.read_csv(R'C:\Users\LENOVO\Desktop\statistic\data\movie_data_cleaned.csv')  
  
# 使用random.sample随机抽取100条数据  
sample = data.sample(n=100)  
  
print(sample)

# 计算均值和标准误差
mean = df_movies['average'].mean()
std_error = stats.sem(df_movies['average'])
# 设定置信水平
confidence_level = 0.95
# 设定自由度
df = len(df_movies['average']) - 1
# 计算置信区间
confidence_interval = stats.t.interval(confidence_level, df, loc=mean, scale=std_error)
# 输出结果
print(F"均值：{mean: .2f}")
print(F"均值在置信水平{confidence_level}下的置信区间为：", confidence_interval)



