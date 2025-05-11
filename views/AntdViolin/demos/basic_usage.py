import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdViolin(
        data=[
            {'x': f'class{i}', 'y': round(random.normalvariate(i, 1), 2)}
            for i in range(1, 6)
            for j in range(50)
        ],
        xField='x',
        yField='y',
        height=500,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdViolin(
    data=[
        {'x': f'class{i}', 'y': round(random.normalvariate(i, 1), 2)}
        for i in range(1, 6)
        for j in range(50)
    ],
    xField='x',
    yField='y',
    height=500,
)
"""
        }
    ]
