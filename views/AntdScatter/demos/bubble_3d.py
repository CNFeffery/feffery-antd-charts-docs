import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdScatter(
        data=[
            {
                'x': random.uniform(-100, 100),
                'y': random.uniform(-100, 100),
                'type': f'class{i % 2 + 1}',
                'value': random.uniform(0, 100),
            }
            for i in range(1, 50)
        ],
        xField='x',
        yField='y',
        colorField='type',
        sizeField='value',
        size=[3, 15],
        color=[
            'r(0.4, 0.3, 0.7) 0:rgba(255,255,255,0.5) 1:#5B8FF9',
            'r(0.4, 0.4, 0.7) 0:rgba(255,255,255,0.5) 1:#61DDAA',
        ],
        shape='circle',
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
            'x': random.uniform(-100, 100),
            'y': random.uniform(-100, 100),
            'type': f'class{i % 2 + 1}',
            'value': random.uniform(0, 100),
        }
        for i in range(1, 50)
    ],
    xField='x',
    yField='y',
    colorField='type',
    sizeField='value',
    size=[3, 15],
    color=[
        'r(0.4, 0.3, 0.7) 0:rgba(255,255,255,0.5) 1:#5B8FF9',
        'r(0.4, 0.4, 0.7) 0:rgba(255,255,255,0.5) 1:#61DDAA',
    ],
    shape='circle',
)
"""
        }
    ]
