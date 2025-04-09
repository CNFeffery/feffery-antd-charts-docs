import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdWaterfall(
        data=[
            {'month': '2019', 'value': 23000000},
            {'month': 'Jan', 'value': 2200000},
            {'month': 'Feb', 'value': -4600000},
            {'month': 'Mar', 'value': -9100000},
            {'month': 'Apr', 'value': 3700000},
            {'month': 'May', 'value': -2100000},
            {'month': 'Jun', 'value': 5300000},
            {'month': 'Jul', 'value': 3100000},
            {'month': 'Aug', 'value': -1500000},
            {'month': 'Sep', 'value': 4200000},
            {'month': 'Oct', 'value': 5300000},
            {'month': 'Nov', 'value': -1500000},
            {'month': 'Dec', 'value': 5100000},
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
            'label': '2020',
        },
        color={
            'func': """
({ month, value }) => {
    if (month === '2019' || month === '2020') {
        return '#96a6a6';
    }

    return value > 0 ? '#f4664a' : '#30bf78';
}
"""
        },
        label={
            'style': {
                'fontSize': 10,
            },
            'layout': [
                {
                    'type': 'interval-adjust-position',
                },
            ],
            'background': {
                'style': {
                    'fill': '#f6f6f6',
                    'stroke': '#e6e6e6',
                    'strokeOpacity': 0.65,
                    'radius': 2,
                },
                'padding': 1.5,
            },
        },
        waterfallStyle={
            'func': """
() => {
    return {
        fillOpacity: 0.85,
    };
}
"""
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': '''
fact.AntdWaterfall(
    data=[
        {'month': '2019', 'value': 23000000},
        {'month': 'Jan', 'value': 2200000},
        {'month': 'Feb', 'value': -4600000},
        {'month': 'Mar', 'value': -9100000},
        {'month': 'Apr', 'value': 3700000},
        {'month': 'May', 'value': -2100000},
        {'month': 'Jun', 'value': 5300000},
        {'month': 'Jul', 'value': 3100000},
        {'month': 'Aug', 'value': -1500000},
        {'month': 'Sep', 'value': 4200000},
        {'month': 'Oct', 'value': 5300000},
        {'month': 'Nov', 'value': -1500000},
        {'month': 'Dec', 'value': 5100000},
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
        'label': '2020',
    },
    color={
        'func': """
({ month, value }) => {
    if (month === '2019' || month === '2020') {
        return '#96a6a6';
    }

    return value > 0 ? '#f4664a' : '#30bf78';
}
"""
    },
    label={
        'style': {
            'fontSize': 10,
        },
        'layout': [
            {
                'type': 'interval-adjust-position',
            },
        ],
        'background': {
            'style': {
                'fill': '#f6f6f6',
                'stroke': '#e6e6e6',
                'strokeOpacity': 0.65,
                'radius': 2,
            },
            'padding': 1.5,
        },
    },
    waterfallStyle={
        'func': """
() => {
    return {
        fillOpacity: 0.85,
    };
}
"""
    },
)
'''
        }
    ]
