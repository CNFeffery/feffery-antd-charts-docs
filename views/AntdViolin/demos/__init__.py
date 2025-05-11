from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    series,  # noqa: F401
    shape_smooth,  # noqa: F401
    shape_hollow,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdViolin')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的小提琴图。',
        },
        {
            'path': 'series',
            'title': '分组小提琴图',
            'description': '针对多系列数据，通过参数`seriesField`设置分组字段。',
        },
        {
            'path': 'shape_smooth',
            'title': 'smooth类型',
            'description': "设置参数`shape='smooth'`时的效果。",
            'group': '小提琴形状类型',
        },
        {
            'path': 'shape_hollow',
            'title': 'hollow类型',
            'description': "设置参数`shape='hollow'`时的效果。",
            'group': '小提琴形状类型',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
