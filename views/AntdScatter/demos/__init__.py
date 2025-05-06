from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    color_mapping,  # noqa: F401
    shape_mapping,  # noqa: F401
    color_and_shape_mapping,  # noqa: F401
    size_mapping,  # noqa: F401
    label,  # noqa: F401
    regression_line,  # noqa: F401
    quadrant,  # noqa: F401
    bubble_3d,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdScatter')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的散点图。',
        },
        {
            'path': 'color_mapping',
            'title': '颜色映射',
            'description': '结合数据和参数`colorField`实现颜色映射。',
        },
        {
            'path': 'shape_mapping',
            'title': '形状映射',
            'description': '结合数据和参数`shapeField`实现形状映射。',
        },
        {
            'path': 'color_and_shape_mapping',
            'title': '颜色和形状映射',
            'description': '同时进行颜色和形状映射。',
        },
        {
            'path': 'size_mapping',
            'title': '尺寸映射',
            'description': '结合数据和参数`sizeField`、`size`、`sizeLegend`实现尺寸映射相关功能。',
        },
        {
            'path': 'label',
            'title': '添加数值标签',
            'description': '通过参数`label`添加数值标签，默认显示`yField`对应值。',
        },
        {
            'path': 'regression_line',
            'title': '添加回归线',
            'description': '通过参数`regressionLine`添加回归线。',
        },
        {
            'path': 'quadrant',
            'title': '添加四象限',
            'description': '通过参数`quadrant`添加四象限。',
        },
        {
            'path': 'bubble_3d',
            'title': '仿3D气泡图',
            'description': '基于参数`color`、`shape`实现仿3D气泡图。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
