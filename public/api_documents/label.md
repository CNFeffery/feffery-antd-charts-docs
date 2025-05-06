- **<placeholder>** 

  *dict*或*bool*型，配置文字标签相关参数，设置为`False`时不显示，支持的键值对属性有：

  - **type** *str*型

    特殊标签类型，如针对饼图可用的`'inner'`、`'outer'`、`'spider'`

  - **offset** *int*、*float*或*str*型

    标签偏移量，支持数值型像素和百分比字符串

  - **offsetX** *int*或*float*型

    标签水平方向像素偏移

  - **offsetY** *int*或*float*型

    标签垂直方向像素偏移

  - **style** *dict*型

    标签文字样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **autoRotate** *bool*型

    是否自动旋转标签

  - **rotate** *int*或*float*型

    标签旋转角度

  - **labelEmit** *bool*型

    极坐标系下有效，设置文本是否按照角度放射状显示

  - **position** *str*型

    文字标签相对于数据点的位置，可选项有`'top'`、`'bottom'`、`'middle'`、`'left'`、`'right'`

  - **layout** *dict*型

    配置文本布局，支持的键值对属性有：

    - **type** *str*型

      文本布局类型，可选项有`'overlap'`、`'fixed-overlap'`、`'limit-in-shape'`

  - **content** *str*型

    配置文本标签内容

  - **formatter** *dict*型

    标签内容`javascript`格式化函数，通过`'func'`字段传入

  - **autoHide** *bool*型，默认值：`False`

    是否自动隐藏标签

  - **background** *dict*型

    配置标签背景，支持的键值对属性有：

    - **style** *dict*型
    
      标签背景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **padding** *int*或*float*型

      标签背景内边距
