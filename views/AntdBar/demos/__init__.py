from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    y_field_as_series,  # noqa: F401
    custom_color,  # noqa: F401
    scrollbar,  # noqa: F401
    conversion_tag,  # noqa: F401
    bar_background,  # noqa: F401
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
        {
            'path': 'custom_color',
            'title': '自定义条形颜色',
            'description': '通过参数`color`自定义控制条形颜色。',
        },
        {
            'path': 'scrollbar',
            'title': '开启滚动条',
            'description': '通过参数`scrollbar`开启滚动条。',
        },
        {
            'path': 'conversion_tag',
            'title': '转换标签',
            'description': '通过参数`conversionTag`添加转换标签。',
        },
        {
            'path': 'bar_background',
            'title': '条形背景',
            'description': '通过参数`barBackground`自定义条形背景。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
