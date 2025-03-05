from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    range_width,  # noqa: F401
    gradient,  # noqa: F401
    custom_color,  # noqa: F401
    custom_color_gradient,  # noqa: F401
    meter_gauge,  # noqa: F401
    indicator_type_cursor,  # noqa: F401
    indicator_type_ring_cursor,  # noqa: F401
    indicator_type_simple,  # noqa: F401
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
        {
            'path': 'custom_color_gradient',
            'title': '多色渐变仪表盘',
            'description': '通过参数`range`自定义多色渐变仪表盘。',
        },
        {
            'path': 'meter_gauge',
            'title': '米轨仪表盘',
            'description': "设置参数`type='meter'`渲染米轨仪表盘。",
        },
        {
            'path': 'indicator_type_cursor',
            'title': 'cursor类型',
            'description': "使用`'cursor'`类型的指示器。",
            'group': '其他指示器类型',
        },
        {
            'path': 'indicator_type_ring_cursor',
            'title': 'ring-cursor类型',
            'description': "使用`'ring-cursor'`类型的指示器。",
            'group': '其他指示器类型',
        },
        {
            'path': 'indicator_type_simple',
            'title': 'simple类型',
            'description': "使用`'simple'`类型的指示器。",
            'group': '其他指示器类型',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
