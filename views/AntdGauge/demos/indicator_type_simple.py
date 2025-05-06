import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdGauge(
        percent=0.78,
        range={
            'color': '#30BF78',
        },
        indicator={
            'shape': 'simple',
            'pointer': {
                'style': {
                    'stroke': '#D0D0D0',
                    'lineWidth': 1,
                    'fill': '#D0D0D0',
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
    percent=0.78,
    range={
        'color': '#30BF78',
    },
    indicator={
        'shape': 'simple',
        'pointer': {
            'style': {
                'stroke': '#D0D0D0',
                'lineWidth': 1,
                'fill': '#D0D0D0',
            },
        },
    },
)
"""
        }
    ]
