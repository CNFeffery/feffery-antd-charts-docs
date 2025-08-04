*dict*型

  定义需要针对当前图表实例执行的动作，每次执行动作后此参数都会被重置为空值，支持的键值对属性有：

  - **type** *str*型

    必填，动作类型，可选项有`'tooltip:show'`、`'tooltip:hide'`

  - **tooltipPositionData** *list*型

    针对`'tooltip:show'`型动作，定义`tooltip`显示位置计算所需的数据信息
