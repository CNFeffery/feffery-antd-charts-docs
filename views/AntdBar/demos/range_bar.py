import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBar(
        data=[
            {
                'type': '分类一',
                'values': [76, 100],
            },
            {
                'type': '分类二',
                'values': [56, 108],
            },
            {
                'type': '分类三',
                'values': [38, 129],
            },
            {
                'type': '分类四',
                'values': [58, 155],
            },
            {
                'type': '分类五',
                'values': [45, 120],
            },
            {
                'type': '分类六',
                'values': [23, 99],
            },
            {
                'type': '分类七',
                'values': [18, 56],
            },
            {
                'type': '分类八',
                'values': [18, 34],
            },
        ],
        xField='values',
        yField='type',
        isRange=True,
        label={
            'position': 'middle',
            'layout': [
                {
                    'type': 'adjust-color',
                },
            ],
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
            'type': '分类一',
            'values': [76, 100],
        },
        {
            'type': '分类二',
            'values': [56, 108],
        },
        {
            'type': '分类三',
            'values': [38, 129],
        },
        {
            'type': '分类四',
            'values': [58, 155],
        },
        {
            'type': '分类五',
            'values': [45, 120],
        },
        {
            'type': '分类六',
            'values': [23, 99],
        },
        {
            'type': '分类七',
            'values': [18, 56],
        },
        {
            'type': '分类八',
            'values': [18, 34],
        },
    ],
    xField='values',
    yField='type',
    isRange=True,
    label={
        'position': 'middle',
        'layout': [
            {
                'type': 'adjust-color',
            },
        ],
    },
)
"""
        }
    ]
