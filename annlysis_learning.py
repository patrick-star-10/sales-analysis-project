import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体,解决中文符号绘图乱码的问题
plt.rcParams['axes.unicode_minus'] = False
file_path = r"sales_data.csv"
def analyze_sales_data(file_path):
    print('---数据加载与初步检查---')
    try:
        df = pd.read_csv(file_path)
        print(f"加载文件 {file_path} 成功")
        print(f"数据形状：{df.shape}")
        print("\n前5行数据:")
        print(df.head(5))
        print("\n数据信息")
        df.info()
    except FileNotFoundError:
        print(f"错误：文件{file_path}未找到，请确保文件存在")
        return 

    print("\n---数据清洗与准备---")
    df['Date'] = pd.to_datetime(df['Date'])
    print("日期列已转化为datetime格式")

    missing_values = df.isnull().sum()
    print("\n检查缺失值")
    print(missing_values[missing_values > 0])
    if missing_values.sum() == 0:
        print("没有缺失值")

    print("\n描述性统计分析")
    print("\n数值列描述性统计：")
    print(df[['Quantity','Price','Sales']].describe())

    total_sales = df['Sales'].sum()
    aov = df['Sales'].mean()
    print(f"总销售额：￥{total_sales:,.2f}")
    print(f"平均订单价值：￥{aov:,.2f}")

    print("\n时间序列分析，月度销售额趋势")
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum()
    monthly_sales.index = monthly_sales.index.astype(str)

    #可视化月度销售额趋势
    plt.figure(figsize=(12,6))
    plt.plot(monthly_sales.index,monthly_sales.values,marker='o',linestyle='-',color='skyblue')
    plt.title('月度销售额趋势')
    plt.xlabel('月份')
    plt.ylabel('销售额(￥)')
    plt.grid(True,linestyle='--',alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
   

    print("\n5.类别分析（按产品类别划分的销售额）")
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
    fig,axes = plt.subplots(1,2,figsize=(15,6))

    axes[0].bar(category_sales.index,category_sales.values,color=['teal','coral','gold'])
    axes[0].set_title('各产品类别总销售额')
    axes[0].set_xlabel('产品类别')
    axes[0].set_ylabel('销售额(￥)')
    axes[0].tick_params(axis='x',rotation=0)
    axes[0].grid(axis='y',linestyle='--',alpha=0.6)

    axes[1].bar(city_sales.index,city_sales.values,color=['lightgreen','orange','violet','lightblue','salmon'])
    axes[1].set_title('各城市类别总销售额')
    axes[1].set_xlabel('产品类别')
    axes[1].set_ylabel('销售额(￥)')
    axes[1].tick_params(axis='x',rotation=0)
    axes[1].grid(axis='y',linestyle='--',alpha=0.6)

    plt.tight_layout()
    
    print('\n分析平均价格与销量的关系')
    product_summary = df.groupby('Product').agg(
        Average_Price = ('Price',np.mean),
        Total_Quantity =('Quantity',np.sum)
    ).reset_index()

    print("\n各产品平均价格与总销量:")
    print(product_summary.sort_values(by='Total_Quantity',ascending=False))

    plt.figure(figsize=(10, 7))
    x = product_summary['Average_Price'].values
    y = product_summary['Total_Quantity'].values
    labels = product_summary['Product'].values

    plt.scatter(x,y,s=y/10,alpha=0.7,c=x,cmap='coolwarm')
    plt.title('产品平均价格与总销量关系')
    plt.xlabel('平均价格(￥)')
    plt.ylabel('总销量')
    plt.colorbar(label='平均价格(￥)')

    for i, label in enumerate(labels):
        plt.annotate(label,(x[i],y[i]),textcoords="offset points",xytext=(5,5),ha='center')

    plt.grid(True,linestyle=':',alpha=0.5)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    analyze_sales_data(file_path)
