from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_style,  # noqa: F401
    group,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdBox')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的箱线图。',
        },
        {
            'path': 'custom_style',
            'title': '自定义样式',
            'description': '通过参数`boxStyle`对箱线图样式进行自定义。',
        },
        {
            'path': 'group',
            'title': '分组箱线图',
            'description': '通过参数`groupField`展示分组箱线图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
