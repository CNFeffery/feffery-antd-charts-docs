import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBar(
        data=[
            {
                'type': '家具家电',
                'sales': 38,
            },
            {
                'type': '粮油副食',
                'sales': 52,
            },
            {
                'type': '生鲜水果',
                'sales': 61,
            },
            {
                'type': '美容洗护',
                'sales': 145,
            },
            {
                'type': '母婴用品',
                'sales': 48,
            },
            {
                'type': '进口食品',
                'sales': 38,
            },
            {
                'type': '食品饮料',
                'sales': 38,
            },
            {
                'type': '家庭清洁',
                'sales': 38,
            },
        ],
        xField='sales',
        yField='type',
        seriesField='type',
        color={
            'func': """
({ type }) => {
    return type === '美容洗护' ? '#FAAD14' : '#5B8FF9';
}
"""
        },
        legend=False,
        meta={
            'type': {
                'alias': '类别',
            },
            'sales': {
                'alias': '销售额',
            },
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
            'type': '家具家电',
            'sales': 38,
        },
        {
            'type': '粮油副食',
            'sales': 52,
        },
        {
            'type': '生鲜水果',
            'sales': 61,
        },
        {
            'type': '美容洗护',
            'sales': 145,
        },
        {
            'type': '母婴用品',
            'sales': 48,
        },
        {
            'type': '进口食品',
            'sales': 38,
        },
        {
            'type': '食品饮料',
            'sales': 38,
        },
        {
            'type': '家庭清洁',
            'sales': 38,
        },
    ],
    xField='sales',
    yField='type',
    seriesField='type',
    color={
        'func': '''
({ type }) => {
    return type === '美容洗护' ? '#FAAD14' : '#5B8FF9';
}
'''
    },
    legend=False,
    meta={
        'type': {
            'alias': '类别',
        },
        'sales': {
            'alias': '销售额',
        },
    },
)
"""
        }
    ]
