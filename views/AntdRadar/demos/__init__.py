from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    min_x,  # noqa: F401
    area_fill,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdRadar')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的雷达图。',
        },
        {
            'path': 'min_x',
            'title': '控制半径轴最小值',
            'description': '通过参数`meta`控制半径轴最小值。',
        },
        {
            'path': 'area_fill',
            'title': '区域填充',
            'description': '通过参数`area`实现区域填充。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
