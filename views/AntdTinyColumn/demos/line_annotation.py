import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdTinyColumn(
        data=[random.randint(50, 100) for _ in range(20)],
        height=60,
        tooltip=False,
        annotations=[
            {
                'type': 'line',
                'start': ['min', 'mean'],
                'end': ['max', 'mean'],
                'text': {
                    'content': '平均值',
                    'offsetY': -2,
                    'style': {
                        'textAlign': 'left',
                        'fontSize': 10,
                        'fill': 'rgba(44, 53, 66, 0.45)',
                        'textBaseline': 'bottom',
                    },
                },
                'style': {
                    'stroke': 'rgba(0, 0, 0, 0.25)',
                },
            },
        ],
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdTinyColumn(
    data=[random.randint(50, 100) for _ in range(20)],
    height=60,
    tooltip=False,
    annotations=[
        {
            'type': 'line',
            'start': ['min', 'mean'],
            'end': ['max', 'mean'],
            'text': {
                'content': '平均值',
                'offsetY': -2,
                'style': {
                    'textAlign': 'left',
                    'fontSize': 10,
                    'fill': 'rgba(44, 53, 66, 0.45)',
                    'textBaseline': 'bottom',
                },
            },
            'style': {
                'stroke': 'rgba(0, 0, 0, 0.25)',
            },
        },
    ],
)
"""
        }
    ]
