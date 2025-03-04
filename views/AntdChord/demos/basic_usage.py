import feffery_antd_charts as fact
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fact.AntdChord(
        data=[
            {'source': '北京', 'target': '天津', 'value': 30},
            {'source': '北京', 'target': '上海', 'value': 80},
            {'source': '北京', 'target': '河北', 'value': 46},
            {'source': '北京', 'target': '辽宁', 'value': 49},
            {'source': '北京', 'target': '黑龙江', 'value': 69},
            {'source': '北京', 'target': '吉林', 'value': 19},
            {'source': '天津', 'target': '河北', 'value': 62},
            {'source': '天津', 'target': '辽宁', 'value': 82},
            {'source': '天津', 'target': '上海', 'value': 16},
            {'source': '上海', 'target': '黑龙江', 'value': 16},
            {'source': '河北', 'target': '黑龙江', 'value': 76},
            {'source': '河北', 'target': '内蒙古', 'value': 24},
            {'source': '内蒙古', 'target': '北京', 'value': 32},
        ],
        sourceField='source',
        targetField='target',
        weightField='value',
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
fact.AntdChord(
    data=[
        {'source': '北京', 'target': '天津', 'value': 30},
        {'source': '北京', 'target': '上海', 'value': 80},
        {'source': '北京', 'target': '河北', 'value': 46},
        {'source': '北京', 'target': '辽宁', 'value': 49},
        {'source': '北京', 'target': '黑龙江', 'value': 69},
        {'source': '北京', 'target': '吉林', 'value': 19},
        {'source': '天津', 'target': '河北', 'value': 62},
        {'source': '天津', 'target': '辽宁', 'value': 82},
        {'source': '天津', 'target': '上海', 'value': 16},
        {'source': '上海', 'target': '黑龙江', 'value': 16},
        {'source': '河北', 'target': '黑龙江', 'value': 76},
        {'source': '河北', 'target': '内蒙古', 'value': 24},
        {'source': '内蒙古', 'target': '北京', 'value': 32},
    ],
    sourceField='source',
    targetField='target',
    weightField='value',
)
"""
        }
    ]
