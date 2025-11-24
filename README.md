# 数据分析实战练习项目：电子产品销售分析

这是一个专为数据分析初学者设计的实战练习项目，旨在帮助您熟悉和掌握 NumPy、Pandas 和 Matplotlib 这三个核心 Python 库在数据分析中的应用。

## 1. 项目目标
- 数据清洗与预处理：学习如何使用 Pandas 加载数据、检查数据类型、处理日期格式。
- 描述性统计：利用 Pandas 和 NumPy 计算关键业务指标（如总销售额、平均订单价值）。
- 数据可视化：使用 Matplotlib 绘制不同维度的图表，直观展示数据洞察。
- 业务分析：通过时间、类别和价格-销量等多个维度对销售数据进行深入分析。

## 2. 文件说明

| 文件名                | 类型       | 描述                                                                 |
| --------------------- | ---------- | -------------------------------------------------------------------- |
| sales_data.csv        | 数据集     | 包含 1000 条模拟电子产品销售记录的 CSV 文件。字段包括：OrderID (订单ID), Date (日期), Product (产品名称), Category (产品类别), City (销售城市), Quantity (数量), Price (单价), Sales (销售额)。 |
| data_analysis.py      | Python代码 | 核心分析脚本，使用 Pandas 进行数据处理，使用 Matplotlib 进行可视化。 |
| monthly_sales_trend.png | 结果图表   | 月度总销售额趋势图。                                                 |
| category_city_sales.png | 结果图表   | 产品类别和城市销售额对比图。                                         |
| price_quantity_scatter.png | 结果图表 | 产品平均价格与总销量关系散点图。                                     |

## 3. 环境准备

在运行分析代码之前，请确保您的 Python 环境中安装了以下库：

```bash
pip install pandas numpy matplotlib
```

## 4. 运行步骤

1. 下载文件：将所有附件（sales_data.csv 和 data_analysis.py）下载到同一个文件夹中。
2. 打开终端/命令行：导航到该文件夹。
3. 执行脚本：运行以下命令执行数据分析脚本：
   ```bash
   python data_analysis.py
   ```
4. 查看结果：脚本将在终端输出分析过程和关键统计结果，并生成三个 PNG 格式的图表文件到当前文件夹。

## 5. 分析要点（供学习参考）

data_analysis.py 脚本中包含了以下几个主要的分析模块：

### 模块一：数据加载与清洗
- 使用 `pd.read_csv()` 加载数据。
- 使用 `df.info()` 和 `df.head()` 进行初步检查。
- 使用 `pd.to_datetime()` 将日期列转换为正确的格式。

### 模块二：时间序列分析
- 通过 `df['Date'].dt.to_period('M')` 提取月份。
- 使用 `df.groupby('Month')['Sales'].sum()` 计算月度销售额。
- 使用 `plt.plot()` 绘制时间趋势图。

### 模块三：类别和地域分析
- 使用 `df.groupby('Category')['Sales'].sum()` 和 `df.groupby('City')['Sales'].sum()` 进行分组聚合。
- 使用 `plt.bar()` 绘制条形图进行对比。

### 模块四：进阶分析（价格与销量关系）
- 使用 `df.groupby('Product').agg(...)` 同时计算每个产品的平均价格 (`np.mean`) 和总销量 (`np.sum`)。
- 使用 `plt.scatter()` 绘制散点图，探索价格和销量之间的潜在关系。
