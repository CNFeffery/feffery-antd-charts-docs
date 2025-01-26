import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdRingProgress(
        height=100,
        width=100,
        autoFit=False,
        percent=0.6,
        color=['#F4664A', '#E8EDF3'],
        innerRadius=0.85,
        radius=0.98,
        statistic={
            'title': {
                'style': {
                    'color': '#363636',
                    'fontSize': '12px',
                    'lineHeight': '14px',
                },
                'formatter': {'func': "() => '进度'"},
            },
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdRingProgress(
    height=100,
    width=100,
    autoFit=False,
    percent=0.6,
    color=['#F4664A', '#E8EDF3'],
    innerRadius=0.85,
    radius=0.98,
    statistic={
        'title': {
            'style': {
                'color': '#363636',
                'fontSize': '12px',
                'lineHeight': '14px',
            },
            'formatter': {'func': "() => '进度'"},
        },
    },
)
"""
        }
    ]
