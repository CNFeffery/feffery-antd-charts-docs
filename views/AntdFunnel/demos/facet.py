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
                'company': 'A公司',
            },
            {
                'stage': '初试人数',
                'number': 151,
                'company': 'A公司',
            },
            {
                'stage': '复试人数',
                'number': 113,
                'company': 'A公司',
            },
            {
                'stage': '录取人数',
                'number': 87,
                'company': 'A公司',
            },
            {
                'stage': '入职人数',
                'number': 59,
                'company': 'A公司',
            },
            {
                'stage': '简历筛选',
                'number': 303,
                'company': 'B公司',
            },
            {
                'stage': '初试人数',
                'number': 251,
                'company': 'B公司',
            },
            {
                'stage': '复试人数',
                'number': 153,
                'company': 'B公司',
            },
            {
                'stage': '录取人数',
                'number': 117,
                'company': 'B公司',
            },
            {
                'stage': '入职人数',
                'number': 79,
                'company': 'B公司',
            },
        ],
        xField='stage',
        yField='number',
        seriesField='company',
        meta={
            'stage': {
                'alias': '行为',
            },
            'pv': {
                'alias': '人数',
                'formatter': {'func': '(v) => `${v}次`'},
            },
        },
        legend=False,
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
            'company': 'A公司',
        },
        {
            'stage': '初试人数',
            'number': 151,
            'company': 'A公司',
        },
        {
            'stage': '复试人数',
            'number': 113,
            'company': 'A公司',
        },
        {
            'stage': '录取人数',
            'number': 87,
            'company': 'A公司',
        },
        {
            'stage': '入职人数',
            'number': 59,
            'company': 'A公司',
        },
        {
            'stage': '简历筛选',
            'number': 303,
            'company': 'B公司',
        },
        {
            'stage': '初试人数',
            'number': 251,
            'company': 'B公司',
        },
        {
            'stage': '复试人数',
            'number': 153,
            'company': 'B公司',
        },
        {
            'stage': '录取人数',
            'number': 117,
            'company': 'B公司',
        },
        {
            'stage': '入职人数',
            'number': 79,
            'company': 'B公司',
        },
    ],
    xField='stage',
    yField='number',
    seriesField='company',
    meta={
        'stage': {
            'alias': '行为',
        },
        'pv': {
            'alias': '人数',
            'formatter': {'func': '(v) => `${v}次`'},
        },
    },
    legend=False,
)
"""
        }
    ]
