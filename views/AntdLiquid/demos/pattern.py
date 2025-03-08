import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdLiquid(
        percent=0.65,
        shape='diamond',
        outline={
            'border': 4,
            'distance': 8,
        },
        wave={
            'length': 128,
        },
        pattern={
            'type': 'line',
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdLiquid(
    percent=0.65,
    shape='diamond',
    outline={
        'border': 4,
        'distance': 8,
    },
    wave={
        'length': 128,
    },
    pattern={
        'type': 'line',
    },
)
"""
        }
    ]
