import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdHeatmap(
        data=[
            {
                'x': f'x{x}',
                'y': f'y{y}',
                'value': round(random.uniform(0, 100), 2),
            }
            for x in range(1, 11)
            for y in range(1, 11)
        ],
        xField='x',
        yField='y',
        colorField='value',
        shape='circle',
        height=800,
        sizeRatio=0.5,
        label={},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdHeatmap(
    data=[
        {
            'x': f'x{x}',
            'y': f'y{y}',
            'value': round(random.uniform(0, 100), 2),
        }
        for x in range(1, 11)
        for y in range(1, 11)
    ],
    xField='x',
    yField='y',
    colorField='value',
    shape='circle',
    height=800,
    sizeRatio=0.5,
    label={},
)
"""
        }
    ]
