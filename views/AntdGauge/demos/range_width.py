import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdGauge(
        percent=0.75,
        range={'color': '#30BF78', 'width': 12},
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
        axis={
            'label': {'formatter': {'func': '(v) => Number(v) * 100'}},
            'subTickLine': {
                'count': 3,
            },
        },
        statistic={
            'content': {
                'formatter': {
                    'func': """({ percent }) => `Rate: ${(percent * 100).toFixed(0)}%`"""
                },
                'style': {
                    'color': 'rgba(0,0,0,0.65)',
                    'fontSize': 28,
                },
            },
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fact.AntdGauge(
    percent=0.75,
    range={'color': '#30BF78', 'width': 12},
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
    axis={
        'label': {'formatter': {'func': '(v) => Number(v) * 100'}},
        'subTickLine': {
            'count': 3,
        },
    },
    statistic={
        'content': {
            'formatter': {
                'func': """({ percent }) => `Rate: ${(percent * 100).toFixed(0)}%`"""
            },
            'style': {
                'color': 'rgba(0,0,0,0.65)',
                'fontSize': 28,
            },
        },
    },
)
'''
        }
    ]
