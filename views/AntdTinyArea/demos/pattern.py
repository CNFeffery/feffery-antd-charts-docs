import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdTinyArea(
        data=[random.randint(50, 100) for _ in range(20)],
        height=60,
        smooth=True,
        color='#E5EDFE',
        pattern={
            'type': 'line',
            'cfg': {
                'stroke': '#5B8FF9',
            },
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdTinyArea(
    data=[random.randint(50, 100) for _ in range(20)],
    height=60,
    smooth=True,
    color='#E5EDFE',
    pattern={
        'type': 'line',
        'cfg': {
            'stroke': '#5B8FF9',
        },
    },
)
"""
        }
    ]
