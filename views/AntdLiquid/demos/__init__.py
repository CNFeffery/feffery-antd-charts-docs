from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    rect,  # noqa: F401
    diamond,  # noqa: F401
    pattern,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdLiquid')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的水波图。',
        },
        {
            'path': 'rect',
            'title': '矩形水波图',
            'description': "设置参数`shape='rect'`渲染矩形水波图。",
        },
        {
            'path': 'diamond',
            'title': '钻石水波图',
            'description': "设置参数`shape='diamond'`渲染钻石水波图。",
        },
        {
            'path': 'pattern',
            'title': '设置填充贴图',
            'description': '通过参数`pattern`设置填充贴图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
