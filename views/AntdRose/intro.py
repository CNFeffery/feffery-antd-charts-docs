import feffery_antd_components as fac
from dash.dependencies import Component

# 国际化
from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('统计图表')},
                {'title': translator.t('AntdRose 风玫瑰图')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdRose 风玫瑰图'), level=2),
        fac.AntdParagraph(translator.t('快捷渲染风玫瑰图。')),
    ]
