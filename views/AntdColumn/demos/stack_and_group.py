import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdColumn(
        data=[
            {
                'date': f'2020-0{i}',
                'y': random.randint(0, 100),
                'type': f'item{j}',
                'series': f'series{k}',
            }
            for i in range(1, 10)
            for j in range(1, 4)
            for k in range(1, 3)
        ],
        xField='date',
        yField='y',
        seriesField='type',
        groupField='series',
        isStack=True,
        isGroup=True,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdColumn(
    data=[
        {
            'date': f'2020-0{i}',
            'y': random.randint(0, 100),
            'type': f'item{j}',
            'series': f'series{k}',
        }
        for i in range(1, 10)
        for j in range(1, 4)
        for k in range(1, 3)
    ],
    xField='date',
    yField='y',
    seriesField='type',
    groupField='series',
    isStack=True,
    isGroup=True,
)
"""
        }
    ]
