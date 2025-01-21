from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    label,  # noqa: F401
    background,  # noqa: F401
    slider,  # noqa: F401
    scrollbar,  # noqa: F401
    conversion_tag,  # noqa: F401
    stack,  # noqa: F401
    stack_connect_area,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdColumn')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的柱状图。',
        },
        {
            'path': 'label',
            'title': '添加数值标签',
            'description': '通过参数`label`添加数值标签。',
        },
        {
            'path': 'background',
            'title': '柱体背景',
            'description': '通过参数`columnBackground`自定义柱体背景。',
        },
        {
            'path': 'slider',
            'title': '开启缩略轴',
            'description': '通过参数`slider`开启缩略轴相关功能。',
        },
        {
            'path': 'scrollbar',
            'title': '开启滚动条',
            'description': '通过参数`scrollbar`开启滚动条。',
        },
        {
            'path': 'conversion_tag',
            'title': '转换标签',
            'description': '通过参数`conversionTag`添加转换标签。',
        },
        {
            'path': 'stack',
            'title': '堆叠柱状图',
            'description': '针对多系列数据，通过参数`seriesField`设置分组字段并设置`isStack=True`后，自动开启堆叠效果。',
        },
        {
            'path': 'stack_connect_area',
            'title': '开启联通区域',
            'description': '针对堆叠柱状图，通过参数`connectedArea`开启联通区域交互功能。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
