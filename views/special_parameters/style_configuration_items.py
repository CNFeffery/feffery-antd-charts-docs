from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component
import feffery_markdown_components as fmc

# 国际化
from i18n import translator

from config import DocsConfig


def render() -> Component:
    """渲染“组件按别名导入”文档页"""

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(duration=0.3),
                    fac.AntdBreadcrumb(
                        items=[
                            {'title': translator.t('特殊参数说明')},
                            {'title': translator.t('样式配置项')},
                        ]
                    ),
                    fac.AntdDivider(isDashed=True),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('fact', code=True),
                            '中各图表组件参数说明所提及的',
                            fac.AntdText('样式配置项', strong=True),
                            '具体可用键值对属性如下：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fmc.FefferyMarkdown(
                        className='side-props-markdown',
                        markdownStr=DocsConfig.props_descriptions['zh-cn'][
                            'base-style'
                        ],
                    ),
                    html.Div(style={'height': 'calc(100vh - 800px)'}),
                ],
                style={'flex': 'auto', 'padding': '25px'},
            )
        ],
        style={'display': 'flex', 'paddingRight': 40},
    )
