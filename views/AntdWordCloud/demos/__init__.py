from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    color,  # noqa: F401
    size_range,  # noqa: F401
    image_mask,  # noqa: F401
    color_field,  # noqa: F401
    multi_class_legend,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdWordCloud')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的词云图。',
        },
        {
            'path': 'color',
            'title': '自定义颜色',
            'description': '通过参数`color`自定义词语颜色。',
        },
        {
            'path': 'size_range',
            'title': '自定义尺寸范围',
            'description': '通过参数`wordStyle`自定义尺寸范围。',
        },
        {
            'path': 'image_mask',
            'title': '自定义图片遮罩',
            'description': '通过参数`imageMask`自定义图片遮罩。',
        },
        {
            'path': 'color_field',
            'title': '使用颜色映射字段',
            'description': '通过参数`colorField`声明颜色映射字段。',
        },
        {
            'path': 'multi_class_legend',
            'title': '多类别图例',
            'description': '具有多类别图例的词云图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
