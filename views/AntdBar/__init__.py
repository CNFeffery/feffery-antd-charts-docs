import feffery_antd_charts as fact
from dash.dependencies import Component

from . import intro, demos
from components import doc_layout


def render() -> Component:
    return doc_layout.render(
        component=fact.AntdBar,
        intro=intro.render(),
        demos=demos.render(component=fact.AntdBar),
        catalog=demos.demos_config,
        component_props=[
            {
                'type': 'props',
                'name': '基础参数',
                'props': [
                    {'name': 'id'},
                    {'name': 'key'},
                    {'name': 'className'},
                    {'name': 'style'},
                    {'name': 'width'},
                    {'name': 'height'},
                    {'name': 'autoFit'},
                    {'name': 'padding'},
                    {'name': 'appendPadding'},
                    {'name': 'renderer'},
                    {'name': 'pixelRatio'},
                    {'name': 'locale'},
                    {'name': 'limitInPlot'},
                    {'name': 'downloadTrigger'},
                ],
            },
            {
                'type': 'props',
                'name': '核心参数',
                'props': [
                    {'name': 'data'},
                    {'name': 'xField'},
                    {'name': 'yField'},
                    {'name': 'seriesField'},
                    {'name': 'groupField', 'source': 'bar-groupField'},
                    {'name': 'isStack'},
                    {'name': 'isGroup', 'source': 'bar-isGroup'},
                    {'name': 'isRange', 'source': 'bar-isRange'},
                    {'name': 'isPercent'},
                    {
                        'name': 'intervalPadding',
                        'source': 'bar-intervalPadding',
                    },
                    {'name': 'dodgePadding', 'source': 'bar-dodgePadding'},
                    {'name': 'minBarWidth'},
                    {'name': 'maxBarWidth'},
                    {'name': 'barBackground'},
                    {'name': 'barWidthRatio'},
                    {'name': 'marginRatio', 'source': 'bar-marginRatio'},
                ],
            },
            {
                'type': 'prop',
                'name': 'color',
                'source': 'base-color',
                'description': '视觉配置参数',
            },
            {
                'type': 'prop',
                'name': 'barStyle',
                'source': 'geometry-style',
                'description': '视觉配置参数',
            },
            {
                'type': 'prop',
                'name': 'conversionTag',
                'description': '特殊功能参数',
            },
            {
                'type': 'prop',
                'name': 'connectedArea',
                'description': '特殊功能参数',
            },
            {
                'type': 'prop',
                'name': 'xAxis',
                'source': 'base-xaxis',
                'description': '坐标轴配置参数',
            },
            {
                'type': 'prop',
                'name': 'yAxis',
                'source': 'base-yaxis',
                'description': '坐标轴配置参数',
            },
            {'type': 'prop', 'name': 'legend', 'description': '图例配置参数'},
            {
                'type': 'prop',
                'name': 'label',
                'description': '数值标签配置参数',
            },
            {
                'type': 'prop',
                'name': 'tooltip',
                'description': '信息框配置参数',
            },
            {
                'type': 'prop',
                'name': 'annotations',
                'description': '标注配置参数',
            },
            {
                'type': 'prop',
                'name': 'animation',
                'description': '动画配置参数',
            },
            {'type': 'prop', 'name': 'theme', 'description': '主题配置参数'},
            {
                'type': 'prop',
                'name': 'interactions',
                'description': '交互功能配置',
            },
            {'type': 'prop', 'name': 'state', 'description': '状态样式配置'},
            {'type': 'prop', 'name': 'pattern', 'description': '填充模式配置'},
            {'type': 'prop', 'name': 'scrollbar', 'description': '滚动条配置'},
            {'type': 'prop', 'name': 'meta', 'description': '字段元配置'},
            {
                'type': 'props',
                'name': '事件监听属性',
                'props': [
                    {'name': 'recentlyTooltipChangeRecord'},
                    {'name': 'recentlyBarClickRecord'},
                    {'name': 'recentlyLegendInfo'},
                ],
            },
        ],
    )
