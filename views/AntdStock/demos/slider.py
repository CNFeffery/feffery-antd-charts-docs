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
        slider={},
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
    slider={},
)
"""
        }
    ]
