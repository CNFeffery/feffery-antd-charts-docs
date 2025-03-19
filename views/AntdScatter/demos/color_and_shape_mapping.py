import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdScatter(
        data=[
            {
                'x': random.uniform(0, 100),
                'y': random.uniform(0, 100),
                'type': f'class{i % 4}',
                'series': f'series{i % 3}',
            }
            for i in range(1, 100)
        ],
        xField='x',
        yField='y',
        colorField='type',
        shapeField='series',
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdScatter(
    data=[
        {
            'x': random.uniform(0, 100),
            'y': random.uniform(0, 100),
            'type': f'class{i % 4}',
            'series': f'series{i % 3}',
        }
        for i in range(1, 100)
    ],
    xField='x',
    yField='y',
    colorField='type',
    shapeField='series',
)
"""
        }
    ]
