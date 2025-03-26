from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_color,  # noqa: F401
    circle_shape,  # noqa: F401
    square_shape,  # noqa: F401
    size,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdHeatmap')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的热力图。',
        },
        {
            'path': 'custom_color',
            'title': '自定义颜色映射',
            'description': '通过参数`color`自定义颜色映射方案。',
        },
        {
            'path': 'circle_shape',
            'title': '圆形热力图',
            'description': '通过参数`shape`设置热力图为圆形热力图，并配合参数`sizeRatio`控制热力圆点比例大小。',
        },
        {
            'path': 'square_shape',
            'title': '方形热力图',
            'description': '通过参数`shape`设置热力图为方形热力图，并配合参数`sizeRatio`控制热力方块比例大小。',
        },
        {
            'path': 'size',
            'title': '尺寸映射',
            'description': '通过参数`sizeField`指定尺寸映射字段。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
