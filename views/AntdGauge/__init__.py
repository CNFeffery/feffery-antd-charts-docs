import feffery_antd_charts as fact
from dash.dependencies import Component

from . import intro, demos
from components import doc_layout


def render() -> Component:
    return doc_layout.render(
        component=fact.AntdGauge,
        intro=intro.render(),
        demos=demos.render(component=fact.AntdGauge),
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
                    {'name': 'percent'},
                    {'name': 'radius'},
                    {'name': 'innerRadius'},
                    {'name': 'startAngle', 'source': 'gauge-startAngle'},
                    {'name': 'endAngle', 'source': 'gauge-endAngle'},
                    {'name': 'range', 'source': 'gauge-range'},
                    {'name': 'type', 'source': 'gauge-type'},
                    {'name': 'meter', 'source': 'gauge-meter'},
                    {'name': 'indicator', 'source': 'gauge-indicator'},
                ],
            },
            {
                'type': 'prop',
                'name': 'gaugeStyle',
                'source': 'geometry-style',
                'description': '视觉配置参数',
            },
            {
                'type': 'prop',
                'name': 'axis',
                'source': 'gauge-axis',
                'description': '坐标轴配置参数',
            },
            {
                'type': 'prop',
                'name': 'statistic',
                'source': 'gauge-statistic',
                'description': '统计配置参数',
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
        ],
    )
