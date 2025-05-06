import math
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdGauge(
        percent=0.75,
        range={
            'color': 'l(0) 0:#B8E1FF 1:#3D76DD',
        },
        startAngle=math.pi,
        endAngle=2 * math.pi,
        indicator=None,
        statistic={
            'title': {
                'offsetY': -36,
                'style': {
                    'fontSize': 28,
                    'color': '#4B535E',
                },
                'formatter': {'func': "() => '70%'"},
            },
            'content': {
                'style': {
                    'fontSize': 28,
                    'lineHeight': '44px',
                    'color': '#4B535E',
                },
                'formatter': {'func': "() => '加载进度'"},
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
        'color': 'l(0) 0:#B8E1FF 1:#3D76DD',
    },
    startAngle=math.pi,
    endAngle=2 * math.pi,
    indicator=None,
    statistic={
        'title': {
            'offsetY': -36,
            'style': {
                'fontSize': 28,
                'color': '#4B535E',
            },
            'formatter': {'func': "() => '70%'"},
        },
        'content': {
            'style': {
                'fontSize': 28,
                'lineHeight': '44px',
                'color': '#4B535E',
            },
            'formatter': {'func': "() => '加载进度'"},
        },
    },
)
"""
        }
    ]
