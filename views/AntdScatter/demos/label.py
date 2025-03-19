import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdScatter(
        data=[
            {
                'x': round(random.uniform(0, 100), 2),
                'y': round(random.uniform(0, 100), 2),
                'type': f'class{i % 4}',
            }
            for i in range(1, 20)
        ],
        xField='x',
        yField='y',
        colorField='type',
        size=5,
        shape='circle',
        pointStyle={
            'fillOpacity': 1,
        },
        yAxis={
            'nice': True,
            'line': {
                'style': {
                    'stroke': '#aaa',
                },
            },
        },
        xAxis={
            'grid': {
                'line': {
                    'style': {
                        'stroke': '#eee',
                    },
                },
            },
            'line': {
                'style': {
                    'stroke': '#aaa',
                },
            },
        },
        label={},
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
            'x': round(random.uniform(0, 100), 2),
            'y': round(random.uniform(0, 100), 2),
            'type': f'class{i % 4}',
        }
        for i in range(1, 20)
    ],
    xField='x',
    yField='y',
    colorField='type',
    size=5,
    shape='circle',
    pointStyle={
        'fillOpacity': 1,
    },
    yAxis={
        'nice': True,
        'line': {
            'style': {
                'stroke': '#aaa',
            },
        },
    },
    xAxis={
        'grid': {
            'line': {
                'style': {
                    'stroke': '#eee',
                },
            },
        },
        'line': {
            'style': {
                'stroke': '#aaa',
            },
        },
    },
    label={},
)
"""
        }
    ]
