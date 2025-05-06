import requests
import feffery_antd_charts as fact
from dash.dependencies import Component

demo_data = requests.get(
    'https://gw.alipayobjects.com/os/antfincdn/%24IWXp5slbE/2020-movie-from-douban.json'
).json()


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdWordCloud(
        data=demo_data,
        wordField='title',
        weightField='rate',
        colorField='tag',
        legend={},
        imageMask='https://gw.alipayobjects.com/zos/antfincdn/Qw7Xbn76kM/53176454-747c-4f0a-a9e5-936aa66a0082.png',
        wordStyle={
            'fontSize': [8, 16],
        },
        height=600,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
demo_data = requests.get(
    'https://gw.alipayobjects.com/os/antfincdn/%24IWXp5slbE/2020-movie-from-douban.json'
).json()

...

fact.AntdWordCloud(
    data=demo_data,
    wordField='title',
    weightField='rate',
    colorField='tag',
    legend={},
    imageMask='https://gw.alipayobjects.com/zos/antfincdn/Qw7Xbn76kM/53176454-747c-4f0a-a9e5-936aa66a0082.png',
    wordStyle={
        'fontSize': [8, 16],
    },
    height=600,
)
"""
        }
    ]
