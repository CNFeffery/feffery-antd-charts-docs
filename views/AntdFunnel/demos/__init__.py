from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    pyramid,  # noqa: F401
    dynamic_height,  # noqa: F401
    compare,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdFunnel')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的漏斗图。',
        },
        {
            'path': 'pyramid',
            'title': '金字塔型漏斗图',
            'description': "设置参数`shape='pyramid'`渲染金字塔型漏斗图。",
        },
        {
            'path': 'dynamic_height',
            'title': '动态高度漏斗图',
            'description': '设置参数`dynamicHeight=True`渲染动态高度漏斗图。',
        },
        {
            'path': 'compare',
            'title': '对比漏斗图',
            'description': '具有对比功能的漏斗图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
