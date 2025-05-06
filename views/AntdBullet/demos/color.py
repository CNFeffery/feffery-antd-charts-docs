import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBullet(
        data=[
            {
                'title': '满意度',
                'ranges': [40, 70, 100],
                'measures': [80],
                'target': 85,
            }
        ],
        measureField='measures',
        rangeField='ranges',
        targetField='target',
        xField='title',
        color={
            'range': ['#FFbcb8', '#FFe0b0', '#bfeec8'],
            'measure': '#5B8FF9',
            'target': '#39a3f4',
        },
        xAxis={'line': None},
        yAxis=False,
        label={'target': True},
        legend={
            'custom': True,
            'position': 'bottom',
            'items': [
                {
                    'value': '差',
                    'name': '差',
                    'marker': {
                        'symbol': 'square',
                        'spacing': 8,
                        'style': {'r': 5, 'fill': '#FFbcb8'},
                    },
                },
                {
                    'value': '良',
                    'name': '良',
                    'marker': {
                        'symbol': 'square',
                        'spacing': 8,
                        'style': {'r': 5, 'fill': '#FFe0b0'},
                    },
                },
                {
                    'value': '优',
                    'name': '优',
                    'marker': {
                        'symbol': 'square',
                        'spacing': 8,
                        'style': {'r': 5, 'fill': '#bfeec8'},
                    },
                },
                {
                    'value': '实际值',
                    'name': '实际值',
                    'marker': {
                        'symbol': 'square',
                        'spacing': 8,
                        'style': {'r': 5, 'fill': '#5B8FF9'},
                    },
                },
                {
                    'value': '目标值',
                    'name': '目标值',
                    'marker': {
                        'symbol': 'line',
                        'style': {
                            'stroke': '#3D76DD',
                            'r': 5,
                        },
                    },
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
fact.AntdBullet(
    data=[
        {
            'title': '满意度',
            'ranges': [40, 70, 100],
            'measures': [80],
            'target': 85,
        }
    ],
    measureField='measures',
    rangeField='ranges',
    targetField='target',
    xField='title',
    color={
        'range': ['#FFbcb8', '#FFe0b0', '#bfeec8'],
        'measure': '#5B8FF9',
        'target': '#39a3f4',
    },
    xAxis={'line': None},
    yAxis=False,
    label={'target': True},
    legend={
        'custom': True,
        'position': 'bottom',
        'items': [
            {
                'value': '差',
                'name': '差',
                'marker': {
                    'symbol': 'square',
                    'spacing': 8,
                    'style': {'r': 5, 'fill': '#FFbcb8'},
                },
            },
            {
                'value': '良',
                'name': '良',
                'marker': {
                    'symbol': 'square',
                    'spacing': 8,
                    'style': {'r': 5, 'fill': '#FFe0b0'},
                },
            },
            {
                'value': '优',
                'name': '优',
                'marker': {
                    'symbol': 'square',
                    'spacing': 8,
                    'style': {'r': 5, 'fill': '#bfeec8'},
                },
            },
            {
                'value': '实际值',
                'name': '实际值',
                'marker': {
                    'symbol': 'square',
                    'spacing': 8,
                    'style': {'r': 5, 'fill': '#5B8FF9'},
                },
            },
            {
                'value': '目标值',
                'name': '目标值',
                'marker': {
                    'symbol': 'line',
                    'style': {
                        'stroke': '#3D76DD',
                        'r': 5,
                    },
                },
            },
        ],
    },
)
"""
        }
    ]
