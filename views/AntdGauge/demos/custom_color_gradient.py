import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdGauge(
        percent=0.75,
        range={
            'ticks': [0, 1],
            'color': ['l(0) 0:#F4664A 0.5:#FAAD14 1:#30BF78'],
        },
        indicator={
            'pointer': {
                'style': {
                    'stroke': '#D0D0D0',
                },
            },
            'pin': {
                'style': {
                    'stroke': '#D0D0D0',
                },
            },
        },
        statistic={
            'content': {
                'style': {
                    'fontSize': '36px',
                    'lineHeight': '36px',
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
fact.AntdGauge(
    percent=0.75,
    range={
        'ticks': [0, 1],
        'color': ['l(0) 0:#F4664A 0.5:#FAAD14 1:#30BF78'],
    },
    indicator={
        'pointer': {
            'style': {
                'stroke': '#D0D0D0',
            },
        },
        'pin': {
            'style': {
                'stroke': '#D0D0D0',
            },
        },
    },
    statistic={
        'content': {
            'style': {
                'fontSize': '36px',
                'lineHeight': '36px',
            },
        },
    },
)
"""
        }
    ]
