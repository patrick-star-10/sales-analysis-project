import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class SaleDataAnalyzer:
    def __init__(self,file_path,output_dir="reports"):
        self.file_path = file_path
        self.output_dir = output_dir
        self.df = None
        self.setup_environment()

    def setup_environment(self):
        if not os.path.exists(self.file_path):
            os.makedirs(self.output_dir)
            print(f"创建输出目录: {self.output_dir}")
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体,解决中文符号绘图乱码的问题
        plt.rcParams['axes.unicode_minus'] = False
        print("环境配置完成(Matplotlib设置 & 输出目录检查)")


    def load_and_clean_data(self):
        print('---数据加载与初步检查---')
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"加载文件 {self.file_path} 成功")
           
            if 'Date' in self.df.columns:
                self.df['Date'] = pd.to_datetime(self.df['Date'])
                print("日期列已转换为datetime格式")

            missing = self.df.isnull().sum().sum()
            if missing == 0:
                print("数据完整性检查通过(无缺失值)")
            else:
                print(f"警告: 发现 {missing} 个缺失值")
            return True
        except FileNotFoundError:
            print(f"错误：文件{self.file_path}未找到，请确保文件存在")
            return False
        except Exception as e:
            print(f"发生未知错误: {e}")
            return False

    def show_basic_stats(self):
        if self.df is None:
            return   
        print("\n数值列描述性统计：")
        print(self.df[['Quantity','Price','Sales']].describe())
        total_sales = self.df['Sales'].sum()
        aov = self.df['Sales'].mean()
        print(f"总销售额：￥{total_sales:,.2f}")
        print(f"平均订单价值：￥{aov:,.2f}")

    def plot_monthly_trend(self):
        if self.df is None: return
        print("\n时间序列分析，月度销售额趋势")
        self.df['Month'] = self.df['Date'].dt.to_period('M')
        monthly_sales = self.df.groupby('Month')['Sales'].sum()
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

        # 保存图表
        save_path = os.path.join(self.output_dir,'monthly_sales_trend.png')
        plt.savefig(save_path)
        print(f"月度销售额趋势图已保存至: {save_path}")
        plt.close()  #关闭画布释放内存
   
    def plot_category_city_analysis(self):
        if self.df is None: return
        print("\n类别分析（按产品类与城市类别划分的销售额）")
        category_sales = self.df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
        city_sales = self.df.groupby('City')['Sales'].sum().sort_values(ascending=False)
        # 可视化类别与城市销售额对比
        fig,axes = plt.subplots(1,2,figsize=(15,6))
        axes[0].bar(category_sales.index,category_sales.values,color=['teal','coral','gold'])
        axes[0].set_title('各产品类别总销售额')
        axes[0].set_xlabel('产品类别')
        axes[0].set_ylabel('销售额(￥)')
        axes[0].tick_params(axis='x',rotation=45)
        axes[0].grid(axis='y',linestyle='--',alpha=0.6)

        axes[1].bar(city_sales.index,city_sales.values,color=['lightgreen','orange','violet','lightblue','salmon'])
        axes[1].set_title('各城市类别总销售额')
        axes[1].set_xlabel('产品类别')
        axes[1].set_ylabel('销售额(￥)')
        axes[1].tick_params(axis='x',rotation=45)
        axes[1].grid(axis='y',linestyle='--',alpha=0.6)

        plt.tight_layout()
        save_path = os.path.join(self.output_dir,'category_city_sales.png')
        plt.savefig(save_path)  
        print(f"类别与城市销售额分析图已保存至: {save_path}")
        plt.close()  #关闭画布释放内存
    def plot_price_quantity_correlation(self):
        if self.df is None: return   
        print('\n分析平均价格与销量的关系')
        product_summary = self.df.groupby('Product').agg(
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

        save_path = os.path.join(self.output_dir,'price_quantity_scatter.png')
        plt.savefig(save_path)  
        print(f"价格与销量关系图已保存至: {save_path}")
        plt.close()  #关闭画布释放内存

    def run_all_analyses(self):
        if self.load_and_clean_data():
            self.show_basic_stats()
            self.plot_monthly_trend()
            self.plot_category_city_analysis()
            self.plot_price_quantity_correlation()
            print("\n所有分析任务已完成")



if __name__ == "__main__":
   DATA_FILE = 'sales_data.csv'  # 假设数据文件名为sales_data.csv
   analyzer = SaleDataAnalyzer(file_path=DATA_FILE,output_dir='reports')
   analyzer.run_all_analyses()
