from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    meta_alias,  # noqa: F401
    slider,  # noqa: F401
    custom_legend,  # noqa: F401
    status_color,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdStock')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的股票图。',
        },
        {
            'path': 'meta_alias',
            'title': '字段别名',
            'description': '通过`meta`参数配置关键字段在图表中显示的别名。',
        },
        {
            'path': 'slider',
            'title': '开启缩略轴',
            'description': '通过参数`slider`开启缩略轴相关功能。',
        },
        {
            'path': 'custom_legend',
            'title': '自定义图例',
            'description': '通过参数`legend`自定义图例，譬如将默认的英文图例项名称替换为中文。',
        },
        {
            'path': 'status_color',
            'title': '自定义状态颜色：绿涨红跌',
            'description': '通过参数`risingFill`、`fallingFill`分别控制上涨、下跌对应状态色。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
