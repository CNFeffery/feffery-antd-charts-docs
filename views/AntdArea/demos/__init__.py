from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    gradient,  # noqa: F401
    slider,  # noqa: F401
    stack,  # noqa: F401
    percent,  # noqa: F401
    df_stack,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdArea')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的面积图。',
        },
        {
            'path': 'gradient',
            'title': '渐变填充',
            'description': '通过参数`areaStyle`实现渐变色填充。',
        },
        {
            'path': 'slider',
            'title': '开启缩略轴',
            'description': '通过参数`slider`开启缩略轴相关功能。',
        },
        {
            'path': 'stack',
            'title': '堆积面积图',
            'description': '针对多系列数据，通过参数`seriesField`设置分组字段，自动开启堆叠效果。',
        },
        {
            'path': 'percent',
            'title': '百分比面积图',
            'description': '针对多系列数据，设置`isPercent=True`启用百分比面积图。',
        },
        {
            'path': 'df_stack',
<<<<<<< HEAD
            'title': 'DataFrame数据格式的堆积面积图',
            'description': '原数据采用常用的DataFrame格式，展示多系列数据的堆积面积图',
=======
            'title': 'DataFrame 堆积面积图',
            'description': '针对多系列数据，利用常用的DataFrame格式数据，展示堆叠效果。',
>>>>>>> 696c4af4596a95255cfc82f2390f6628fb78d061
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
