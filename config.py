import os
import json
import feffery_antd_charts as fact

# 国际化
from i18n import translator


class DeployConfig:
    """
    应用部署相关参数
    """

    # CDN模块名列表
    cdn_modules = [
        'DashRenderer',
        'dash_html_components',
        'dash_core_components',
        'feffery_antd_charts',
        'feffery_antd_components',
        'feffery_utils_components',
        'feffery_markdown_components',
    ]


class AppConfig:
    """
    应用常规参数配置
    """

    # 应用默认标签页标题
    title = 'feffery-antd-charts在线文档'

    # 应用logo地址
    logo_path = 'imgs/fact-logo.svg'

    # 页首标题
    page_header_title = 'feffery-antd-charts'

    # 当前组件版本
    library_version = fact.__version__

    # 组件仓库地址
    library_repo = 'https://github.com/CNFeffery/feffery-antd-charts'

    # 文档仓库地址
    doc_library_repo = 'https://github.com/CNFeffery/feffery-antd-charts-docs'

    # 文档Gitee仓库地址
    doc_gitee_library_repo = (
        'https://gitee.com/cnfeffery/feffery-antd-charts-docs'
    )

    # 文档仓库分支名称
    doc_library_branch = 'main'

    # 当前应用是否为正式发布模式
    is_release = True

    # 文档贡献者信息
    doc_contributors = json.load(open('./public/contributors.json'))

    # 项目国际化指南地址
    i18n_guide_link = (
        'https://github.com/CNFeffery/feffery-antd-docs/issues/166'
    )

    @staticmethod
    def side_menu_items() -> list:
        # 侧边菜单栏数据结构
        return [
            {
                'component': 'ItemGroup',
                'props': {'key': '快速入门', 'title': translator.t('快速入门')},
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/what-is-fact',
                            'name': '/what-is-fact',
                            'href': '/what-is-fact',
                            'title': translator.t('fact是什么'),
                        },
                    }
                ],
            },
            {'component': 'Divider', 'props': {'dashed': True}},
            {
                'component': 'ItemGroup',
                'props': {'key': '组件介绍', 'title': translator.t('组件介绍')},
                'children': [
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '统计图表',
                            'title': translator.t('统计图表'),
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdLine',
                                    'name': '/AntdLine',
                                    'title': translator.t('AntdLine 折线图'),
                                    'href': '/AntdLine',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdArea',
                                    'name': '/AntdArea',
                                    'title': translator.t('AntdArea 面积图'),
                                    'href': '/AntdArea',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdColumn',
                                    'name': '/AntdColumn',
                                    'title': translator.t('AntdColumn 柱状图'),
                                    'href': '/AntdColumn',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdBar',
                                    'name': '/AntdBar',
                                    'title': translator.t('AntdBar 条形图'),
                                    'href': '/AntdBar',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdPie',
                                    'name': '/AntdPie',
                                    'title': translator.t('AntdPie 饼图'),
                                    'href': '/AntdPie',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdDualAxes',
                                    'name': '/AntdDualAxes',
                                    'title': translator.t(
                                        'AntdDualAxes 双轴图'
                                    ),
                                    'href': '/AntdDualAxes',
                                },
                            },
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': '迷你图',
                                    'title': translator.t('迷你图'),
                                },
                                'children': [
                                    {
                                        'component': 'Item',
                                        'props': {
                                            'key': '/AntdTinyLine',
                                            'name': '/AntdTinyLine',
                                            'title': translator.t(
                                                'AntdTinyLine 迷你折线图'
                                            ),
                                            'href': '/AntdTinyLine',
                                        },
                                    },
                                    {
                                        'component': 'Item',
                                        'props': {
                                            'key': '/AntdTinyArea',
                                            'name': '/AntdTinyArea',
                                            'title': translator.t(
                                                'AntdTinyArea 迷你面积图'
                                            ),
                                            'href': '/AntdTinyArea',
                                        },
                                    },
                                    {
                                        'component': 'Item',
                                        'props': {
                                            'key': '/AntdTinyColumn',
                                            'name': '/AntdTinyColumn',
                                            'title': translator.t(
                                                'AntdTinyColumn 迷你柱状图'
                                            ),
                                            'href': '/AntdTinyColumn',
                                        },
                                    },
                                    {
                                        'component': 'Item',
                                        'props': {
                                            'key': '/AntdProgress',
                                            'name': '/AntdProgress',
                                            'title': translator.t(
                                                'AntdProgress 进度条图'
                                            ),
                                            'href': '/AntdProgress',
                                        },
                                    },
                                    {
                                        'component': 'Item',
                                        'props': {
                                            'key': '/AntdRingProgress',
                                            'name': '/AntdRingProgress',
                                            'title': translator.t(
                                                'AntdRingProgress 进度环图'
                                            ),
                                            'href': '/AntdRingProgress',
                                        },
                                    },
                                ],
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdStock',
                                    'name': '/AntdStock',
                                    'title': translator.t('AntdStock 股票图'),
                                    'href': '/AntdStock',
                                },
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/AntdFunnel',
                                    'name': '/AntdFunnel',
                                    'title': translator.t('AntdFunnel 漏斗图'),
                                    'href': '/AntdFunnel',
                                },
                            },
                        ],
                    },
                ],
            },
            {
                'component': 'ItemGroup',
                'props': {
                    'key': '特殊参数说明',
                    'title': translator.t('特殊参数说明'),
                },
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/style',
                            'name': '/style',
                            'title': translator.t('样式配置项'),
                            'href': '/style',
                        },
                    }
                ],
            },
        ]

    # 侧边菜单栏key值 -> 展开项节点key值数组
    side_menu_expand_keys = {
        '/AntdLine': ['统计图表'],
        '/AntdArea': ['统计图表'],
        '/AntdColumn': ['统计图表'],
        '/AntdBar': ['统计图表'],
        '/AntdPie': ['统计图表'],
        '/AntdDualAxes': ['统计图表'],
        '/AntdStock': ['统计图表'],
        '/AntdTinyLine': ['统计图表', '迷你图'],
        '/AntdTinyArea': ['统计图表', '迷你图'],
        '/AntdTinyColumn': ['统计图表', '迷你图'],
        '/AntdProgress': ['统计图表', '迷你图'],
        '/AntdRingProgress': ['统计图表', '迷你图'],
        '/AntdFunnel': ['统计图表'],
    }


class DocsConfig:
    """
    文档所需特殊参数配置
    """

    # 具有额外参数说明的组件
    components_with_extra_params = []

    # 参数说明映射
    props_descriptions = {
        'zh-cn': {
            file.split('.')[0]: (
                open(
                    os.path.join('./public/api_documents', file),
                    encoding='utf-8',
                )
                .read()
                .replace('- **<placeholder>**', '')
            )
            for file in os.listdir('./public/api_documents')
            if file.endswith('.md')
        },
        'en-us': {
            file.split('.')[0]: (
                open(
                    os.path.join('./public/api_documents/en_us', file),
                    encoding='utf-8',
                )
                .read()
                .replace('- **<placeholder>**', '')
            )
            for file in os.listdir('./public/api_documents/en_us')
            if file.endswith('.md')
        },
    }
