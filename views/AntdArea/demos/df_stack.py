import random
import pandas as pd
import feffery_antd_charts as fact
from dash.dependencies import Component

# 构造演示用例相关内容

# 2. 读取数据 含有时间、地区、人数三列
df = pd.read_excel('assets//source_data.xlsx', sheet_name='Area')

# 3. 处理为AntdArea组件可用的格式
chart_data = [
    {
        'date': row['时间'],
        'y': row['人数'],
        'type': row['地区'],
    }
    for _, row in df.iterrows()
]


def render() -> Component:
    """渲染当前演示用例"""

    demo_contents = fact.AntdArea(
        data=chart_data,
        xField='date',  # x轴字段
        yField='y',  # y轴字段
        seriesField='type',  # 分类字段
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
# 1. 导入所需的库
import dash
import pandas as pd
import feffery_antd_charts as fact


# 2. 读取数据为DataFrame格式(假设我们的Excel文件名为source, sheet名为Area, 且表含有时间、地区、人数三列)
df = pd.read_excel("source_data.xlsx", sheet_name="Area")

# 若转为字典，具体是这样的：
# df_dict ={
#     "时间": {0: "2023-01-01",
#         1: "2023-01-01",
#         2: "2023-01-01",
#         3: "2023-01-02",
#         4: "2023-01-02",
#         5: "2023-01-02",
#         6: "2023-01-03",
#         7: "2023-01-03",
#         8: "2023-01-03",
#         9: "2023-01-04",
#         10: "2023-01-04",
#         11: "2023-01-04",
#         12: "2023-01-05",
#         13: "2023-01-05",
#         14: "2023-01-05",
#         15: "2023-01-06",
#         16: "2023-01-06",
#         17: "2023-01-06",
#         18: "2023-01-07",
#         19: "2023-01-07",
#         20: "2023-01-07",
#         21: "2023-01-08",
#         22: "2023-01-08",
#         23: "2023-01-08",
#         24: "2023-01-09",
#         25: "2023-01-09",
#         26: "2023-01-09",
#         27: "2023-01-10",
#         28: "2023-01-10",
#         29: "2023-01-10",
#     },
#     "人数": {
#         0: 87,
#         1: 64,
#         2: 63,
#         3: 87,
#         4: 5,
#         5: 2,
#         6: 96,
#         7: 38,
#         8: 67,
#         9: 30,
#         10: 28,
#         11: 12,
#         12: 4,
#         13: 18,
#         14: 97,
#         15: 48,
#         16: 6,
#         17: 7,
#         18: 73,
#         19: 95,
#         20: 9,
#         21: 84,
#         22: 37,
#         23: 13,
#         24: 62,
#         25: 38,
#         26: 85,
#         27: 56,
#         28: 42,
#         29: 36,
#     },
#     "地区": {
#         0: "北京",
#         1: "上海",
#         2: "广州",
#         3: "北京",
#         4: "上海",
#         5: "广州",
#         6: "北京",
#         7: "上海",
#         8: "广州",
#         9: "北京",
#         10: "上海",
#         11: "广州",
#         12: "北京",
#         13: "上海",
#         14: "广州",
#         15: "北京",
#         16: "上海",
#         17: "广州",
#         18: "北京",
#         19: "上海",
#         20: "广州",
#         21: "北京",
#         22: "上海",
#         23: "广州",
#         24: "北京",
#         25: "上海",
#         26: "广州",
#         27: "北京",
#         28: "上海",
#         29: "广州",
#     },
# }


# 3. 将DataFrame格式的数据处理为AntdArea组件可用的格式
chart_data = [
    {
        "date": row["时间"],
        "y": row["人数"],
        "type": row["地区"],
    }
    for _, row in df.iterrows()
]

# 4. 创建Dash应用
app = dash.Dash(__name__)

# 5. 设置图表布局
app.layout = fact.AntdArea(
    data=chart_data,
    xField="date",  # x轴字段
    yField="y",  # y轴字段
    seriesField="type",  # 分类字段
)

# 6. 在jupyterlab中运行应用
if __name__ == "__main__":
    app.run(jupyter_mode="inline", port=8051)
"""
        }
    ]
