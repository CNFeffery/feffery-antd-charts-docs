import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdWaterfall(
        data=[
            {
                'type': '日用品',
                'money': 120,
            },
            {
                'type': '伙食费',
                'money': 900,
            },
            {
                'type': '交通费',
                'money': 200,
            },
            {
                'type': '水电费',
                'money': 300,
            },
            {
                'type': '房租',
                'money': 1200,
            },
            {
                'type': '商场消费',
                'money': 1000,
            },
            {
                'type': '红包收入',
                'money': -2000,
            },
        ],
        xField='type',
        yField='money',
        meta={
            'type': {
                'alias': '类别',
            },
            'money': {'alias': '收支'},
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
        {
            'type': '日用品',
            'money': 120,
        },
        {
            'type': '伙食费',
            'money': 900,
        },
        {
            'type': '交通费',
            'money': 200,
        },
        {
            'type': '水电费',
            'money': 300,
        },
        {
            'type': '房租',
            'money': 1200,
        },
        {
            'type': '商场消费',
            'money': 1000,
        },
        {
            'type': '红包收入',
            'money': -2000,
        },
    ],
    xField='type',
    yField='money',
    meta={
        'type': {
            'alias': '类别',
        },
        'money': {'alias': '收支'},
    },
)
"""
        }
    ]
