# 本脚本是针对中国新冠病毒各省市历史发病数据的清洗工具
# 作者 https://github.com/Avens666  mail: cz_666@qq.com
# 数据源使用 https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/csv/DXYArea.csv
# 输入源数据来自 data_step1.py 的输出文件
# 本脚本基于data_step1.py的输出 计算每天的新增数据，源数据只有每天的累计确诊数据，本脚本通过当天数据减去前一天数据的方式，计算出每天新增数据
# 用户通过修改 inputfile  和  outputfile 定义源数据文件和输出文件

from datetime import timedelta

import pandas

inputfile = "data/out_2.20.csv"
outputfile = "data/out_increase_province_2.20.csv"
# 显示所有列
pandas.set_option('display.max_columns', None)
# 显示所有行
pandas.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pandas.set_option('max_colwidth', 200)

# ！！！ 根据需要选择合适的字符集
try:
    dataf = pandas.read_csv(inputfile, encoding='UTF-8', usecols=range(1, 10))
except:
    dataf = pandas.read_csv(inputfile, encoding='gb2312', usecols=range(1, 10))

# 计算增量 根据日期间隔计算

dataf['日期'] = pandas.to_datetime(dataf['日期'], format='%Y-%m-%d')  # 1900 -> 2020

df_t = dataf['日期']
df_date = df_t.drop_duplicates()  # 去重 这个返回Series对象

df_t = dataf['省']
df_province = df_t.drop_duplicates()  # 去重 返回所有的省的列表

# dataf['新增确诊'] = dataf['确诊']
dataf.insert(loc=5, column='新增确诊', value=0)
dataf.insert(loc=6, column='新增治愈', value=0)
dataf.insert(loc=7, column='新增死亡', value=0)

# 删除市信息
dataf.drop(['市', '确诊', '治愈', '死亡'], axis=1, inplace=True)
# print(dataf.head())
# df_date = df_date.sort_values(ascending=False)
cur_date = df_date.min()

df = pandas.DataFrame()

for province_t in df_province:
    for date_t in df_date:
        print(province_t, date_t)
        df1 = dataf.loc[(dataf['省'].str.contains(province_t)) & (dataf['日期'] == date_t), :]
        if df1.shape[0] == 0:
            d = {
                '日期': date_t,
                '省': province_t,
                '省确诊': 0,
                '省治愈': 0,
                '省死亡': 0,
                '新增确诊': 0,
                '新增治愈': 0,
                '新增死亡': 0,
            }
            df1 = pandas.DataFrame(d, index=[0])

        else:
            index_0 = df1.iloc[:, 0].index[0]
            if date_t != cur_date:
                data2 = dataf.loc[(dataf['省'].str.contains(province_t)) & (dataf['日期'] == date_t - timedelta(days=1)),
                        :]
                if data2.shape[0] > 0:
                    df1.loc[index_0, '新增确诊'] = df1.loc[index_0, '省确诊'] - data2.iloc[0, :]['省确诊']
                    df1.loc[index_0, '新增治愈'] = df1.loc[index_0, '省治愈'] - data2.iloc[0, :]['省治愈']
                    df1.loc[index_0, '新增死亡'] = df1.loc[index_0, '省死亡'] - data2.iloc[0, :]['省死亡']
                else:
                    df1.loc[index_0, '新增确诊'] = df1.loc[index_0, '省确诊']
                    df1.loc[index_0, '新增治愈'] = df1.loc[index_0, '省治愈']
                    df1.loc[index_0, '新增死亡'] = df1.loc[index_0, '省死亡']
            else:
                df1.loc[index_0, '新增确诊'] = df1.loc[index_0, '省确诊']
                df1.loc[index_0, '新增治愈'] = df1.loc[index_0, '省治愈']
                df1.loc[index_0, '新增死亡'] = df1.loc[index_0, '省死亡']
        # print(df1.iloc[0,:])
        df = df.append(df1.iloc[0, :])
print(df)
df.to_csv(outputfile, encoding="utf_8_sig")  # 为保证excel打开兼容，输出为UTF8带签名格式
