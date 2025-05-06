import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdColumn(
        data=[
            {
                'x': f'item{i}',
                'y': random.randint(50, 100),
            }
            for i in range(1, 100)
        ],
        xField='x',
        yField='y',
        scrollbar={},
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
            'x': f'item{i}',
            'y': random.randint(50, 100),
        }
        for i in range(1, 100)
    ],
    xField='x',
    yField='y',
    scrollbar={},
)
"""
        }
    ]
