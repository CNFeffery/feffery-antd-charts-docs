from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    spider_label,  # noqa: F401
    inner_label,  # noqa: F401
    custom_label_content,  # noqa: F401
    angle_range,  # noqa: F401
    donut,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdPie')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的饼图。',
        },
        {
            'path': 'spider_label',
            'title': '蜘蛛型标签布局',
            'description': '通过参数`label`配置使用蜘蛛型标签布局。',
        },
        {
            'path': 'inner_label',
            'title': '内部型标签布局',
            'description': '通过参数`label`配置使用内部型标签布局。',
        },
        {
            'path': 'custom_label_content',
            'title': '自定义标签内容',
            'description': '通过参数`label.formatter`配置自定义标签内容显示逻辑。',
        },
        {
            'path': 'angle_range',
            'title': '设置角度范围',
            'description': '通过参数`startAngle`和`endAngle`设置角度范围。',
        },
        {
            'path': 'donut',
            'title': '环图',
            'description': '设置参数`innerRadius`启用环图效果。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
