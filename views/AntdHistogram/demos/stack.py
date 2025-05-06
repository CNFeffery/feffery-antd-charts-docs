import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdHistogram(
        data=[
            *[
                {
                    'value': round(random.normalvariate(100, 10), 2),
                    'series': 'A',
                }
                for i in range(1, 100)
            ],
            *[
                {
                    'value': round(random.normalvariate(100, 10), 2),
                    'series': 'B',
                }
                for i in range(1, 50)
            ],
            *[
                {
                    'value': round(random.normalvariate(100, 10), 2),
                    'series': 'C',
                }
                for i in range(1, 20)
            ],
        ],
        binField='value',
        stackField='series',
        binWidth=5,
        legend={},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdHistogram(
    data=[
        *[
            {
                'value': round(random.normalvariate(100, 10), 2),
                'series': 'A',
            }
            for i in range(1, 100)
        ],
        *[
            {
                'value': round(random.normalvariate(100, 10), 2),
                'series': 'B',
            }
            for i in range(1, 50)
        ],
        *[
            {
                'value': round(random.normalvariate(100, 10), 2),
                'series': 'C',
            }
            for i in range(1, 20)
        ],
    ],
    binField='value',
    stackField='series',
    binWidth=5,
    legend={},
)
"""
        }
    ]
