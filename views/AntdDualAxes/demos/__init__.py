from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    line_and_column,  # noqa: F401
    dual_line_style,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdDualAxes')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的双轴图。',
        },
        {
            'path': 'line_and_column',
            'title': '柱线混合',
            'description': '柱体+折线混合双轴图。',
        },
        {
            'path': 'dual_line_style',
            'title': '折线双轴图自定义样式',
            'description': '针对折线双轴图，自定义折线样式。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
