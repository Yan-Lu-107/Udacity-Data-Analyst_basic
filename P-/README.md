## UDACITY Data Analysis Nanodegree Project: Exploring Weather Trends.
# Overview
In this project, I analyzed local and global temperature data and compare the temperature trends for the closest city from where i live which is 'Shanghai' to overall global temperature trends.

# Description
In the report, I visualize the data and describe the similarities and differences between the global temperature trend and the temperature trend of Shanghai. 

# Progress outline:

Extract data from the database.
Write SQL query, extract city data and global data, and export to CSV file.
Open the CSV with Excel, and create a line graph to compare the temperature in Shanghai with the global temperature. 
Draw a moving average instead of an annual average, make the line smooth and make the temperature trend easier to observe
Observe the similarities and differences between the average temperature of the world and the average temperature of Shanghai, as well as the overall trend. 
I made an observation and conclusion about the data, like:
Compared with the global average temperature, is the average temperature in your city hotter or colder? Are the long-term temperature differences consistent?
"Over the long term, how does the temperature change in your city compare to the global average temperature change?"
What is the overall trend? Is the world getting hotter or colder? Is the temperature trend consistent with the trend in the past few hundred years?

More details are existed in the Report file.



Summary
In this project, i analyzed local and global temperature data and compare the temperature trends for the closest city from where i live which is 'Cairo' to overall global temperature trends.
The city i live in was not exist in the data so i used the closest city to my country .
The goal is to create a visualization and prepare a write up describing the similarities and differences between global temperature trends and temperature trends in the closest big city to where i live.
INTRODUCTION:
SQL Query was used to download (CSV) file that contains yearly average temperature of the City ‘Cairo’ and the global temperature.
Then the data has been analyzed using Python Programming Language using IPython Notebook (Jupyter).
Progress outline:
Extract the data :
• Downloading 2 data files from SQL database as CSV.
Create a line chart :
• Calculating the Moving Average (Rolling Average) to make it easier to observe the trends when it be shown in Charts.
• Visualizing the Data Using matplotlib
Make observations :
• I made observations the i saw related to the data "you can find more details on the Report file"
• I made a conclusion about the data.
more details are existed in the Report file.


# 概览
在这个项目中，我们将分析本地和全球的气温数据，并比较你居住地的气温走向与全球气温走向。

# 说明
你的任务是让数据可视化，描述全球气温走向和最接近你居住地的大城市气温走向之间的相似性与差异。所以需要按照以下步骤操作：

从数据库中 提取数据。我们将在下一节介绍一个工作区，这个工作区与数据库连接。你需要导出世界气温数据以及最接近你居住地的大城市气温数据。city_list 表是城市和国家列表。想要与数据库交互，就需要编写一个 SQL 查询。
编写 SQL 查询，提取城市数据，导出到 CSV 文件。
编写一个 SQL 查询来提取全球数据，并导出到 CSV 文件。
用任何你喜欢使用的工具打开 CSV，建议使用 Excel 或 Google 表格，但也欢迎使用其他工具，如 Python 或 R。
创建一个线条图，将你所在城市的气温与全球气温比较。确保绘制 移动平均值 而不是年平均值，使线条平滑，使气温走向便于观察
观察 世界平均气温与你所在城市平均气温之间的相似性和差异，以及整体趋势。
