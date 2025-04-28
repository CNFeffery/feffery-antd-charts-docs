import random
import numpy as np
import feffery_antd_charts as fact
from dash.dependencies import Component

from feffery_dash_utils.component_prop_utils import to_box_data


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdBox(
        data=[
            {
                'x': f'series{i}',
                **to_box_data(
                    np.random.normal(
                        random.uniform(50, 100), random.randint(5, 20), 100
                    )
                ),
            }
            for i in range(1, 6)
        ],
        xField='x',
        yField=['low', 'q1', 'median', 'q3', 'high'],
        boxStyle={
            'stroke': '#545454',
            'fill': '#1890FF',
            'fillOpacity': 0.3,
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
from feffery_dash_utils.component_prop_utils import to_box_data

...

fact.AntdBox(
    data=[
        {
            'x': f'series{i}',
            **to_box_data(
                np.random.normal(
                    random.uniform(50, 100), random.randint(5, 20), 100
                )
            ),
        }
        for i in range(1, 6)
    ],
    xField='x',
    yField=['low', 'q1', 'median', 'q3', 'high'],
    boxStyle={
        'stroke': '#545454',
        'fill': '#1890FF',
        'fillOpacity': 0.3,
    },
)
"""
        }
    ]
