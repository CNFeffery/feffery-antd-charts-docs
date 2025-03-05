from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    range_width,  # noqa: F401
    gradient,  # noqa: F401
    custom_color,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdGauge')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的仪表盘。',
        },
        {
            'path': 'range_width',
            'title': '设置辅助圆弧宽度',
            'description': '通过参数`range`自定义辅助圆弧宽度。',
        },
        {
            'path': 'gradient',
            'title': '渐变填充',
            'description': '通过参数`range`实现辅助圆弧渐变色填充。',
        },
        {
            'path': 'custom_color',
            'title': '多色仪表盘',
            'description': '通过参数`range`自定义多色仪表盘。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
