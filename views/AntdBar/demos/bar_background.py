import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBar(
        data=[
            {
                'type': f'item{i}',
                'x': random.randint(50, 100),
            }
            for i in range(1, 6)
        ],
        xField='x',
        yField='type',
        barBackground={
            'style': {
                'fill': 'rgba(99, 149, 250, 0.3)',
            },
        },
        interactions=[
            {
                'type': 'active-region',
                'enable': False,
            },
        ],
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdBar(
    data=[
        {
            'type': f'item{i}',
            'x': random.randint(50, 100),
        }
        for i in range(1, 6)
    ],
    xField='x',
    yField='type',
    barBackground={
        'style': {
            'fill': 'rgba(99, 149, 250, 0.3)',
        },
    },
    interactions=[
        {
            'type': 'active-region',
            'enable': False,
        },
    ],
)
"""
        }
    ]
