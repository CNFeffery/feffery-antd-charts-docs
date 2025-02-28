import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdFunnel(
        data=[
            {
                'stage': '简历筛选',
                'number': 253,
            },
            {
                'stage': '初试人数',
                'number': 151,
            },
            {
                'stage': '复试人数',
                'number': 113,
            },
            {
                'stage': '录取人数',
                'number': 87,
            },
            {
                'stage': '入职人数',
                'number': 59,
            },
        ],
        xField='stage',
        yField='number',
        legend=False,
        dynamicHeight=True,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdFunnel(
    data=[
        {
            'stage': '简历筛选',
            'number': 253,
        },
        {
            'stage': '初试人数',
            'number': 151,
        },
        {
            'stage': '复试人数',
            'number': 113,
        },
        {
            'stage': '录取人数',
            'number': 87,
        },
        {
            'stage': '入职人数',
            'number': 59,
        },
    ],
    xField='stage',
    yField='number',
    legend=False,
    dynamicHeight=True,
)
"""
        }
    ]
