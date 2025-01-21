import feffery_antd_charts as fact
from dash.dependencies import Component
from feffery_antd_charts.demo_data import stock_data


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdStock(
        data=stock_data,
        xField='trade_date',
        yField=['open', 'close', 'high', 'low'],
        meta={
            'vol': {
                'alias': '成交量',
            },
            'open': {
                'alias': '开盘价',
            },
            'close': {
                'alias': '收盘价',
            },
            'high': {
                'alias': '最高价',
            },
            'low': {
                'alias': '最低价',
            },
        },
        tooltip={
            'fields': ['open', 'close', 'high', 'low', 'vol'],
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
from feffery_antd_charts.demo_data import stock_data

...

fact.AntdStock(
    data=stock_data,
    xField='trade_date',
    yField=['open', 'close', 'high', 'low'],
    meta={
        'vol': {
            'alias': '成交量',
        },
        'open': {
            'alias': '开盘价',
        },
        'close': {
            'alias': '收盘价',
        },
        'high': {
            'alias': '最高价',
        },
        'low': {
            'alias': '最低价',
        },
    },
    tooltip={
        'fields': ['open', 'close', 'high', 'low', 'vol'],
    },
)
"""
        }
    ]
