# 销售数据分析工具 - README

## 项目简介

销售数据分析工具（Sales Data Analyzer）是一个基于 Python 的自动化数据分析脚本，能够对销售数据进行清洗、统计分析和可视化展示。该工具提供了一站式的数据分析流程，帮助用户快速洞察销售趋势、产品类别表现和城市销售分布等关键业务指标。

## 功能特性

- **数据加载与清洗**：自动读取 CSV 格式的销售数据，处理日期格式并检查数据完整性
- **基础统计分析**：生成销售额、订单量等关键指标的描述性统计
- **可视化分析**：
  - 月度销售趋势图
  - 产品类别与城市销售额对比图
  - 价格-销量关系散点图
- **自动化报告生成**：自动创建输出目录并保存所有分析图表

## 环境要求

### 依赖库

本项目基于 Python 开发，已经过以下库版本的测试：

NumPy: 2.3.2
Pandas: 2.3.2
Matplotlib: 3.10.7

### 安装依赖

```bash
pip install pandas numpy matplotlib
```

## 数据格式要求

输入数据需为 CSV 格式，建议包含以下列：

| 列名       | 数据类型    | 说明                 |
|------------|-------------|----------------------|
| Date       | 日期        | 销售日期（如：2023-01-01） |
| Product    | 字符串      | 产品名称             |
| Category   | 字符串      | 产品类别             |
| City       | 字符串      | 销售城市             |
| Quantity   | 数值        | 销售数量             |
| Price      | 数值        | 单价                 |
| Sales      | 数值        | 销售额（Quantity × Price） |

示例数据：

```csv
Date,Product,Category,City,Quantity,Price,Sales
2023-01-01,Product A,Electronics,Shanghai,5,100,500
2023-01-02,Product B,Clothing,Beijing,3,200,600
```

## 使用方法

### 1. 准备数据

将您的销售数据保存为 `sales_data.csv` 文件，放在脚本同一目录下，或修改代码中的文件路径。

### 2. 运行脚本

```bash
python sales_analyzer.py
```

### 3. 查看结果

- 控制台会输出数据分析过程和关键统计指标
- 生成的图表会保存在自动创建的 `reports` 目录下

## 输出文件说明

运行完成后，`reports` 目录中将包含以下文件：

1. **monthly_sales_trend.png** - 月度销售额趋势折线图
2. **category_city_sales.png** - 产品类别与城市销售额对比柱状图
3. **price_quantity_scatter.png** - 产品价格与销量关系散点图

## 代码结构

```
SalesDataAnalyzer/
├── __init__()          # 初始化类，设置路径和环境
├── _setup_environment()# 配置绘图环境和创建输出目录
├── load_and_clean_data() # 加载并预处理数据
├── show_basic_stats()  # 展示基础统计信息
├── plot_monthly_trend() # 生成月度趋势图
├── plot_category_city_analysis() # 生成类别与城市分析图
├── plot_price_quantity_relation() # 生成价格销量关系图
└── run_pipeline()      # 执行完整分析流程
```

## 自定义配置

### 修改数据文件路径

```python
# 在主程序入口处修改 DATA_FILE 变量
DATA_FILE = r"path/to/your/sales_data.csv"
```

### 修改输出目录

```python
# 实例化时指定 output_dir 参数
analyzer = SalesDataAnalyzer(file_path=DATA_FILE, output_dir="your_report_dir")
```

### 调整图表样式

可以修改 `_setup_environment()` 方法中的 matplotlib 参数来自定义图表样式：

```python
# 修改字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使用微软雅黑
# 修改图表大小
plt.figure(figsize=(14, 8))  # 在绘图方法中调整
```

## 常见问题

### Q: 运行时出现中文字体显示方块怎么办？

A: 修改 `_setup_environment()` 方法中的字体设置，使用系统中存在的中文字体：

```python
# Windows 系统
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
# macOS 系统
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti TC']
# Linux 系统
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
```

### Q: 提示文件未找到错误？

A: 请检查：
1. 数据文件路径是否正确
2. 文件扩展名是否正确（应为.csv）
3. 文件是否存在于指定路径下

### Q: 图表保存失败？

A: 请确保：
1. 脚本所在目录有写入权限
2. 输出目录名称不包含特殊字符
3. 磁盘空间充足

## 扩展建议

1. **添加更多分析维度**：
   - 周度/季度销售分析
   - 客户细分分析
   - 利润率分析

2. **增强数据处理能力**：
   - 处理重复数据
   - 异常值检测与处理
   - 数据标准化

3. **输出格式扩展**：
   - 生成 PDF 报告
   - 导出 Excel 格式的统计结果
   - 生成交互式可视化（使用 Plotly）

4. **自动化部署**：
   - 设置定时任务自动运行
   - 集成到数据管道中
   - 生成邮件报告

## 总结

- 该工具提供了一个完整的销售数据分析流程，涵盖数据加载、清洗、分析和可视化
- 代码采用面向对象设计，易于扩展和维护
- 支持自定义配置，可根据实际需求调整分析维度和输出格式
- 生成的可视化图表直观展示关键业务指标，帮助快速做出数据驱动的决策
