from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    non_gradient,  # noqa: F401
    pattern,  # noqa: F401
    line_annotation,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdTinyArea')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '最基础的迷你面积图。',
        },
        {
            'path': 'non_gradient',
            'title': '非渐变填充',
            'description': '通过参数`areaStyle`设置填充色后，默认的渐变填充效果将关闭。',
        },
        {
            'path': 'pattern',
            'title': '填充图案',
            'description': '通过参数`pattern`设置填充图案。',
        },
        {
            'path': 'line_annotation',
            'title': '添加标注线',
            'description': '通过参数`annotations`添加辅助标注线。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
