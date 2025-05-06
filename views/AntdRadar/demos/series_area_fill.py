import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdRadar(
        data=[
            {
                'class': f'class{i}',
                'series': f'series{j}',
                'value': random.randint(50, 100),
            }
            for i in range(1, 10)
            for j in range(1, 3)
        ],
        xField='class',
        yField='value',
        seriesField='series',
        radius=0.9,
        meta={'value': {'min': 0}},
        area={},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdRadar(
    data=[
        {
            'class': f'class{i}',
            'series': f'series{j}',
            'value': random.randint(50, 100),
        }
        for i in range(1, 10)
        for j in range(1, 3)
    ],
    xField='class',
    yField='value',
    seriesField='series',
    radius=0.9,
    meta={'value': {'min': 0}},
    area={},
)
"""
        }
    ]
