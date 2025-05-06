import numpy as np
import pandas as pd
import feffery_antd_charts as fact
from dash.dependencies import Component

# 构造演示用例相关内容
dates = pd.date_range(start='2023-01-01', periods=7, freq='D').strftime(
    '%Y-%m-%d'
)
regions = ['北京', '上海', '广州']
data = []

for date in dates:
    for region in regions:
        data.append(
            {'时间': date, '地区': region, '人数': np.random.randint(10, 100)}
        )
df = pd.DataFrame(data)


chart_data = [
    {
        'date': row['时间'],
        'x': row['人数'],
        'type': row['地区'],
    }
    for _, row in df.iterrows()
]


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBar(
        data=chart_data,
        xField='x',
        yField='date',
        seriesField='type',
        isGroup=True,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
import pandas as pd
import numpy as np

# 1.构造演示用模拟DataFrame格式数据
dates = pd.date_range(start="2023-01-01", periods=7, freq="D").strftime("%Y-%m-%d")
regions = ["北京", "上海", "广州"]
data = []

for date in dates:
    for region in regions:
        data.append({"时间": date, "地区": region, "人数": np.random.randint(10, 100)})

df = pd.DataFrame(data)


# 2. 将DataFrame格式的数据处理为可用的格式
chart_data = [
    {
        "date": row["时间"],
        "x": row["人数"],
        "type": row["地区"],
    }
    for _, row in df.iterrows()
]

# 3. 设置图表布局
fact.AntdBar(
    data= chart_data,
    xField="x",
    yField="date",
    seriesField="type",
    isGroup=True,
)
"""
        }
    ]
