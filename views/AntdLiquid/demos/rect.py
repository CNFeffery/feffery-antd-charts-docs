import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdLiquid(
        percent=0.25,
        shape='rect',
        outline={
            'border': 4,
            'distance': 8,
        },
        wave={
            'length': 128,
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdLiquid(
    percent=0.25,
    shape='rect',
    outline={
        'border': 4,
        'distance': 8,
    },
    wave={
        'length': 128,
    },
)
"""
        }
    ]
