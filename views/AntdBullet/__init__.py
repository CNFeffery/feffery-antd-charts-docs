import feffery_antd_charts as fact
from dash.dependencies import Component

from . import intro, demos
from components import doc_layout


def render() -> Component:
    return doc_layout.render(
        component=fact.AntdBullet,
        intro=intro.render(),
        demos=demos.render(component=fact.AntdBullet),
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
                    {'name': 'data', 'source': 'bullet-data'},
                    {'name': 'measureField', 'source': 'bullet-measureField'},
                    {'name': 'rangeField', 'source': 'bullet-rangeField'},
                    {'name': 'targetField', 'source': 'bullet-targetField'},
                    {'name': 'xField', 'source': 'bullet-xField'},
                    {'name': 'layout', 'source': 'bullet-layout'},
                    {'name': 'size', 'source': 'bullet-size'},
                ],
            },
            {
                'type': 'prop',
                'name': 'color',
                'source': 'bullet-color',
                'description': '视觉配置参数',
            },
            {
                'type': 'prop',
                'name': 'bulletStyle',
                'source': 'bullet-style',
                'description': '视觉配置参数',
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
                'source': 'bullet-label',
                'description': '数值标签配置参数',
            },
            {
                'type': 'prop',
                'name': 'tooltip',
                'description': '信息框配置参数',
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
            {'type': 'prop', 'name': 'meta', 'description': '字段元配置'},
        ],
    )
