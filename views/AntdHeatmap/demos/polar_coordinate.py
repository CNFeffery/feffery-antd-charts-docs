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
        color=['#BAE7FF', '#1890FF', '#1028ff'],
        coordinate={
            'type': 'polar',
            'cfg': {
                'innerRadius': 0.2,
            },
        },
        height=700,
        xAxis={
            'line': None,
            'grid': None,
            'tickLine': None,
            'label': {
                'offset': 12,
                'style': {
                    'fill': '#666',
                    'fontSize': 12,
                    'textBaseline': 'top',
                },
            },
        },
        yAxis={
            'top': True,
            'line': None,
            'grid': None,
            'tickLine': None,
            'label': {
                'offset': 0,
                'style': {
                    'fill': '#fff',
                    'textAlign': 'center',
                    'shadowBlur': 2,
                    'shadowColor': 'rgba(0, 0, 0, .45)',
                },
            },
        },
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
    color=['#BAE7FF', '#1890FF', '#1028ff'],
    coordinate={
        'type': 'polar',
        'cfg': {
            'innerRadius': 0.2,
        },
    },
    height=700,
    xAxis={
        'line': None,
        'grid': None,
        'tickLine': None,
        'label': {
            'offset': 12,
            'style': {
                'fill': '#666',
                'fontSize': 12,
                'textBaseline': 'top',
            },
        },
    },
    yAxis={
        'top': True,
        'line': None,
        'grid': None,
        'tickLine': None,
        'label': {
            'offset': 0,
            'style': {
                'fill': '#fff',
                'textAlign': 'center',
                'shadowBlur': 2,
                'shadowColor': 'rgba(0, 0, 0, .45)',
            },
        },
    },
)
"""
        }
    ]
