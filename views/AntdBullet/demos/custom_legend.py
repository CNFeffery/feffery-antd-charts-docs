import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBullet(
        data=[
            {
                'title': '满意度',
                'ranges': [100],
                'measures': [80],
                'target': 85,
            },
        ],
        measureField='measures',
        rangeField='ranges',
        targetField='target',
        xField='title',
        color={
            'range': '#f0efff',
            'measure': '#5B8FF9',
            'target': '#3D76DD',
        },
        xAxis={
            'line': None,
        },
        legend={
            'custom': True,
            'position': 'bottom',
            'items': [
                {
                    'value': '实际值',
                    'name': '实际值',
                    'marker': {
                        'symbol': 'square',
                        'style': {
                            'fill': '#5B8FF9',
                            'r': 5,
                        },
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
            'ranges': [100],
            'measures': [80],
            'target': 85,
        },
    ],
    measureField='measures',
    rangeField='ranges',
    targetField='target',
    xField='title',
    color={
        'range': '#f0efff',
        'measure': '#5B8FF9',
        'target': '#3D76DD',
    },
    xAxis={
        'line': None,
    },
    legend={
        'custom': True,
        'position': 'bottom',
        'items': [
            {
                'value': '实际值',
                'name': '实际值',
                'marker': {
                    'symbol': 'square',
                    'style': {
                        'fill': '#5B8FF9',
                        'r': 5,
                    },
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
