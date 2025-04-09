from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_total,  # noqa: F401
    custom_label,  # noqa: F401
    absolute_value_label,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdWaterfall')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的瀑布图。',
        },
        {
            'path': 'custom_total',
            'title': '自定义总计值显示',
            'description': '通过参数`total`自定义总计值显示。',
        },
        {
            'path': 'custom_label',
            'title': '自定义数值标签',
            'description': '基于参数`label`、`meta`自定义配置数值标签显示。',
        },
        {
            'path': 'absolute_value_label',
            'title': '绝对值数值标签',
            'description': "设置参数`labelMode='absolute'`开启绝对值数值标签显示模式。",
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
