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
