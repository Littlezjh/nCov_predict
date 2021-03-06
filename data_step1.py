# 本脚本是针对中国新冠病毒各省市历史发病数据的清洗工具
# 作者 https://github.com/Avens666  mail: cz_666@qq.com
# 源数据来自 https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/csv/DXYArea.csv
# 本脚本将各省市每天的数据进行去重处理，每个省市只保留最新的一条数据 （也可选择保留当天最大数值）
# 用户通过修改 inputfile  和  outputfile 定义源数据文件和输出文件

import pandas

inputfile = "data/data_2.20.csv"
outputfile = "data/out_2.20.csv"
# pandas显示配置 方便调试
# 列名对齐
pandas.set_option('display.unicode.ambiguous_as_wide', True)
pandas.set_option('display.unicode.east_asian_width', True)
# 显示所有列
pandas.set_option('display.max_columns', None)
# 显示所有行
pandas.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pandas.set_option('max_colwidth', 300)


# ！！！ 根据需要选择合适的字符集
try:
    dataf = pandas.read_csv(inputfile, encoding='UTF-8')
except:
    dataf = pandas.read_csv(inputfile, encoding='gb2312')


dataf['updateTime'] = pandas.to_datetime(dataf['updateTime'])
dataf['date'] = dataf['updateTime'].apply(lambda x: x.strftime('%Y-%m-%d'))
# print(type(dataf))  print(dataf.dtypes)   print(dataf.head())

# 提取省列表
df_t = dataf['provinceName']
df_province = df_t.drop_duplicates()  # 去重 这个返回Series对象
# df_province = df_t.unique()  # 去重 这个返回 ndarray


df = pandas.DataFrame()

df_t = dataf['date']
df_date = df_t.drop_duplicates()  # 去重 这个返回Series对象

for date_t in df_date:
    for name in df_province:
        print(date_t + name)  # 输出处理进度
        df1 = dataf.loc[(dataf['provinceName'].str.contains(name)) & (dataf['date'].str.contains(date_t)), :]

        df_t = df1['cityName']
        df_city = df_t.drop_duplicates()  # 去重 这个返回Series对象
        province_confirmedCount = df1['province_confirmedCount'].max()
        province_curedCount = df1['province_curedCount'].max()
        province_deadCount = df1['province_deadCount'].max()

        for city in df_city:
            df2 = df1.loc[(df1['cityName'].str.contains(city)), :]  #df2筛选出某个市的数据

#使用当天最后时间的数据，注释这行，则使用当天最大值提取数据
            df2 = df2.loc[(df2['updateTime'] == df2['updateTime'].max()), :]

            new = pandas.DataFrame({'省': name,
                                    '省确诊': province_confirmedCount,
                                    '省治愈': province_curedCount,
                                    '省死亡': province_deadCount,
                                    '市': city,
                                    '确诊': df2['city_confirmedCount'].max(),
                                    '治愈': df2['city_curedCount'].max(),
                                    '死亡': df2['city_deadCount'].max(),
                                    '日期': date_t},
                                   pandas.Index(range(1)))
            # print(new.head())
            df = df.append(new)

# print(df)
cols=['日期','省','省确诊','省治愈','省死亡','市','确诊','治愈','死亡']
df.to_csv(outputfile, encoding="utf_8_sig",columns=cols) #为保证excel打开兼容，输出为UTF8带签名格式

