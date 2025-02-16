import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBar(
        data=[
            {
                'date': f'2020-0{i}',
                'x': random.randint(0, 100),
                'type': f'item{j}',
            }
            for i in range(1, 10)
            for j in range(1, 4)
        ],
        xField='x',
        yField='date',
        seriesField='type',
        isStack=True,
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
            'date': f'2020-0{i}',
            'x': random.randint(0, 100),
            'type': f'item{j}',
        }
        for i in range(1, 10)
        for j in range(1, 4)
    ],
    xField='x',
    yField='date',
    seriesField='type',
    isStack=True,
)
"""
        }
    ]
