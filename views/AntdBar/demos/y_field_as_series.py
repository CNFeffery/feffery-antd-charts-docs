import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBar(
        data=[
            {
                'year': '1951 年',
                'value': 38,
            },
            {
                'year': '1952 年',
                'value': 52,
            },
            {
                'year': '1956 年',
                'value': 61,
            },
            {
                'year': '1957 年',
                'value': 145,
            },
            {
                'year': '1958 年',
                'value': 48,
            },
        ],
        xField='value',
        yField='year',
        seriesField='year',
        legend={
            'position': 'top-left',
        },
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
            'year': '1951 年',
            'value': 38,
        },
        {
            'year': '1952 年',
            'value': 52,
        },
        {
            'year': '1956 年',
            'value': 61,
        },
        {
            'year': '1957 年',
            'value': 145,
        },
        {
            'year': '1958 年',
            'value': 48,
        },
    ],
    xField='value',
    yField='year',
    seriesField='year',
    legend={
        'position': 'top-left',
    },
)
"""
        }
    ]
