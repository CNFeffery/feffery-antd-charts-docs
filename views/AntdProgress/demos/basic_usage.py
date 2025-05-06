import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdProgress(
        height=60, percent=0.7, color=['#5B8FF9', '#E8EDF3']
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdProgress(
    height=60, percent=0.7, color=['#5B8FF9', '#E8EDF3']
)
"""
        }
    ]
