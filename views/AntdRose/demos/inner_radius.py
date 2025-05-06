import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdRose(
        data=[
            {
                'class': f'class{i}',
                'value': random.randint(50, 100),
            }
            for i in range(1, 10)
        ],
        xField='class',
        yField='value',
        seriesField='class',
        radius=0.9,
        innerRadius=0.4,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdRose(
    data=[
        {
            'class': f'class{i}',
            'value': random.randint(50, 100),
        }
        for i in range(1, 10)
    ],
    xField='class',
    yField='value',
    seriesField='class',
    radius=0.9,
    innerRadius=0.4,
)
"""
        }
    ]
