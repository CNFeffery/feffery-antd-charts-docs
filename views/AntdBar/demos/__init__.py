from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    y_field_as_series,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdBar')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的条形图。',
        },
        {
            'path': 'y_field_as_series',
            'title': 'y轴字段作为分组字段',
            'description': '`yField`和`seriesField`参数相同时，每个条形将进行颜色区分。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
