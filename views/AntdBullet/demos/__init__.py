from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_legend,  # noqa: F401
    vertical,  # noqa: F401
    color,  # noqa: F401
    stacked,  # noqa: F401
    grouped,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdBullet')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的子弹图。',
        },
        {
            'path': 'custom_legend',
            'title': '自定义图例',
            'description': '通过参数`legend`为子弹图配置图例。',
        },
        {
            'path': 'vertical',
            'title': '垂直子弹图',
            'description': '垂直形式的子弹图。',
        },
        {
            'path': 'color',
            'title': '多颜色范围区间',
            'description': '为子弹图配置多个颜色范围区间。',
        },
        {
            'path': 'stacked',
            'title': '堆叠子弹图',
            'description': '堆叠形式的子弹图。',
        },
        {
            'path': 'grouped',
            'title': '分组子弹图',
            'description': '分组形式的子弹图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
