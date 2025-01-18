from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    smooth,  # noqa: F401
    custom_point,  # noqa: F401
    slider,  # noqa: F401
    series,  # noqa: F401
    step,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdLine')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的折线图。',
        },
        {
            'path': 'smooth',
            'title': '平滑折线',
            'description': '设置参数`smooth=True`启用平滑折线。',
        },
        {
            'path': 'custom_point',
            'title': '折点自定义配置',
            'description': '通过参数`point`对折点进行自定义配置。',
        },
        {
            'path': 'slider',
            'title': '开启缩略轴',
            'description': '通过参数`slider`开启缩略轴相关功能。',
        },
        {
            'path': 'series',
            'title': '分组折线',
            'description': '设置参数`seriesField`指定分组字段。',
        },
        {
            'path': 'step',
            'title': '阶梯折线图',
            'description': '通过参数`stepType`配置阶梯折线图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
