import random
import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    demo_words = [
        'China',
        'India',
        'United States',
        'Indonesia',
        'Brazil',
        'Pakistan',
        'Nigeria',
        'Bangladesh',
        'Russia',
        'Japan',
        'Mexico',
        'Ethiopia',
        'Philippines',
        'Egypt',
        'Vietnam',
        'Germany',
        'Democratic Republic of the Congo',
        'Iran',
        'Turkey',
        'Thailand',
        'France',
        'United Kingdom',
        'Italy',
        'Tanzania',
        'South Africa',
        'Myanmar',
        'South Korea',
        'Colombia',
        'Kenya',
        'Spain',
        'Argentina',
        'Ukraine',
        'Sudan',
        'Uganda',
        'Algeria',
        'Poland',
        'Iraq',
        'Canada',
        'Morocco',
        'Saudi Arabia',
        'Uzbekistan',
        'Malaysia',
        'Peru',
        'Venezuela',
        'Nepal',
        'Angola',
        'Ghana',
        'Yemen',
        'Afghanistan',
        'Mozambique',
    ]

    # 构造演示用例相关内容
    demo_contents = fact.AntdWordCloud(
        data=[
            {'word': word, 'value': random.randint(10, 100) ** 3}
            for word in demo_words
        ],
        wordField='word',
        weightField='value',
        color='#122c6a',
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
demo_words = [
    'China',
    'India',
    'United States',
    'Indonesia',
    'Brazil',
    'Pakistan',
    'Nigeria',
    'Bangladesh',
    'Russia',
    'Japan',
    'Mexico',
    'Ethiopia',
    'Philippines',
    'Egypt',
    'Vietnam',
    'Germany',
    'Democratic Republic of the Congo',
    'Iran',
    'Turkey',
    'Thailand',
    'France',
    'United Kingdom',
    'Italy',
    'Tanzania',
    'South Africa',
    'Myanmar',
    'South Korea',
    'Colombia',
    'Kenya',
    'Spain',
    'Argentina',
    'Ukraine',
    'Sudan',
    'Uganda',
    'Algeria',
    'Poland',
    'Iraq',
    'Canada',
    'Morocco',
    'Saudi Arabia',
    'Uzbekistan',
    'Malaysia',
    'Peru',
    'Venezuela',
    'Nepal',
    'Angola',
    'Ghana',
    'Yemen',
    'Afghanistan',
    'Mozambique',
]

...

fact.AntdWordCloud(
        data=[
        {'word': word, 'value': random.randint(10, 100) ** 3}
        for word in demo_words
    ],
    wordField='word',
    weightField='value',
    color='#122c6a',
)
"""
        }
    ]
