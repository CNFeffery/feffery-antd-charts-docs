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
            }
            for i in range(1, 100)
        ],
        xField='x',
        yField='y',
        quadrant={
            'xBaseline': 0,
            'yBaseline': 0,
            'labels': [
                {
                    'content': '第一象限',
                },
                {
                    'content': '第二象限',
                },
                {
                    'content': '第三象限',
                },
                {
                    'content': '第四象限',
                },
            ],
        },
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
        }
        for i in range(1, 100)
    ],
    xField='x',
    yField='y',
    quadrant={
        'xBaseline': 0,
        'yBaseline': 0,
        'labels': [
            {
                'content': '第一象限',
            },
            {
                'content': '第二象限',
            },
            {
                'content': '第三象限',
            },
            {
                'content': '第四象限',
            },
        ],
    },
)
"""
        }
    ]
