import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdWaterfall(
        data=[
            {'month': '一月', 'value': 6200000},
            {'month': '二月', 'value': -600000},
            {'month': '三月', 'value': -4100000},
            {'month': '四月', 'value': 3700000},
            {'month': '五月', 'value': -2100000},
            {'month': '六月', 'value': 5300000},
            {'month': '七月', 'value': 3100000},
            {'month': '八月', 'value': -500000},
            {'month': '九月', 'value': 4200000},
            {'month': '十月', 'value': 5300000},
            {'month': '十一月', 'value': -500000},
            {'month': '十二月', 'value': 5100000},
        ],
        xField='month',
        yField='value',
        meta={
            'month': {
                'alias': '月份',
            },
            'value': {
                'alias': '销售量',
                'formatter': {'func': '(v) => `${v / 10000000} 亿`'},
            },
        },
        total={
            'label': '总计',
            'style': {
                'fill': '#96a6a6',
            },
        },
        labelMode='absolute',
        label={
            'style': {
                'fontSize': 10,
            },
            'background': {
                'style': {
                    'fill': '#f6f6f6',
                    'radius': 1,
                },
                'padding': 1.5,
            },
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdWaterfall(
    data=[
        {'month': '一月', 'value': 6200000},
        {'month': '二月', 'value': -600000},
        {'month': '三月', 'value': -4100000},
        {'month': '四月', 'value': 3700000},
        {'month': '五月', 'value': -2100000},
        {'month': '六月', 'value': 5300000},
        {'month': '七月', 'value': 3100000},
        {'month': '八月', 'value': -500000},
        {'month': '九月', 'value': 4200000},
        {'month': '十月', 'value': 5300000},
        {'month': '十一月', 'value': -500000},
        {'month': '十二月', 'value': 5100000},
    ],
    xField='month',
    yField='value',
    meta={
        'month': {
            'alias': '月份',
        },
        'value': {
            'alias': '销售量',
            'formatter': {'func': '(v) => `${v / 10000000} 亿`'},
        },
    },
    total={
        'label': '总计',
        'style': {
            'fill': '#96a6a6',
        },
    },
    labelMode='absolute',
    label={
        'style': {
            'fontSize': 10,
        },
        'background': {
            'style': {
                'fill': '#f6f6f6',
                'radius': 1,
            },
            'padding': 1.5,
        },
    },
)
"""
        }
    ]
