import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdPie(
        data=[
            {
                'type': f'item{i}',
                'x': random.randint(50, 100),
            }
            for i in range(1, 6)
        ],
        colorField='type',
        angleField='x',
        radius=0.9,
        label={
            'formatter': {
                'func': '({ percent }) => `${(percent * 100).toFixed(0)}%`'
            }
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdPie(
    data=[
        {
            'type': f'item{i}',
            'x': random.randint(50, 100),
        }
        for i in range(1, 6)
    ],
    colorField='type',
    angleField='x',
    radius=0.9,
    label={
        'formatter': {
            'func': '({ percent }) => `${(percent * 100).toFixed(0)}%`'
        }
    },
)
"""
        }
    ]
