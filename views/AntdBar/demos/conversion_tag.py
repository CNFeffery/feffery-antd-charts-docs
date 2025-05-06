import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBar(
        data=[
            {
                'action': '浏览网站',
                'pv': 50000,
            },
            {
                'action': '放入购物车',
                'pv': 35000,
            },
            {
                'action': '生成订单',
                'pv': 25000,
            },
            {
                'action': '支付订单',
                'pv': 15000,
            },
            {
                'action': '完成交易',
                'pv': 8500,
            },
        ],
        xField='pv',
        yField='action',
        conversionTag={},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdBar(
    data=[
        {
            'action': '浏览网站',
            'pv': 50000,
        },
        {
            'action': '放入购物车',
            'pv': 35000,
        },
        {
            'action': '生成订单',
            'pv': 25000,
        },
        {
            'action': '支付订单',
            'pv': 15000,
        },
        {
            'action': '完成交易',
            'pv': 8500,
        },
    ],
    xField='pv',
    yField='action',
    conversionTag={},
)
"""
        }
    ]
