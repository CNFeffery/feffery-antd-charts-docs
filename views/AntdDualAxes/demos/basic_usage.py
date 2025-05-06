import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdDualAxes(
        data=[
            # 左轴数据
            [
                {
                    'date': f'2020-0{i}',
                    'y1': random.randint(50, 100),
                }
                for i in range(1, 10)
            ],
            # 右轴数据
            [
                {
                    'date': f'2020-0{i}',
                    'y2': random.randint(100, 1000),
                }
                for i in range(1, 10)
            ],
        ],
        xField='date',
        yField=['y1', 'y2'],
        geometryOptions=[{'geometry': 'line'}, {'geometry': 'line'}],
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdDualAxes(
    data=[
        # 左轴数据
        [
            {
                'date': f'2020-0{i}',
                'y1': random.randint(50, 100),
            }
            for i in range(1, 10)
        ],
        # 右轴数据
        [
            {
                'date': f'2020-0{i}',
                'y2': random.randint(100, 1000),
            }
            for i in range(1, 10)
        ],
    ],
    xField='date',
    yField=['y1', 'y2'],
    geometryOptions=[{'geometry': 'line'}, {'geometry': 'line'}],
)
"""
        }
    ]
