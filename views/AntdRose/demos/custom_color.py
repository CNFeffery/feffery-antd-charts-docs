import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdRose(
        data=sorted(
            [
                {
                    'class': f'c{i}',
                    'value': random.randint(0, 100),
                }
                for i in range(1, 51)
            ],
            key=lambda x: x['value'],
            reverse=True,
        ),
        xField='class',
        yField='value',
        seriesField='class',
        innerRadius=0.1,
        color=[f'rgba(24, 144, 255, {1 - i / 50})' for i in range(1, 51)],
        label=False,
        legend=False,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdRose(
    data=sorted(
        [
            {
                'class': f'c{i}',
                'value': random.randint(0, 100),
            }
            for i in range(1, 51)
        ],
        key=lambda x: x['value'],
        reverse=True,
    ),
    xField='class',
    yField='value',
    seriesField='class',
    innerRadius=0.1,
    color=[f'rgba(24, 144, 255, {1 - i / 50})' for i in range(1, 51)],
    label=False,
    legend=False,
)
"""
        }
    ]
