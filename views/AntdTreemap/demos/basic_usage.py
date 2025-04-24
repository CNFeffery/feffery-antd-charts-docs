import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdTreemap(
        data={
            'name': '根节点',
            'children': [
                {
                    'name': f'item{i}',
                    'value': random.randint(20, 100),
                }
                for i in range(1, 11)
            ],
        },
        colorField='name',
        height=600,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdTreemap(
    data={
        'name': '根节点',
        'children': [
            {
                'name': f'item{i}',
                'value': random.randint(20, 100),
            }
            for i in range(1, 11)
        ],
    },
    colorField='name',
)
"""
        }
    ]
