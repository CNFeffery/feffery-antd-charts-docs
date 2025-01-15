- **<placeholder>** 

  *list*或*bool*型，配置需要添加的标注，每个标注项为字典，支持的键值对属性有：

  - **type** *str*型

    当前标注类型，可选项有`'text'`、`'line'`、`'image'`、`'region'`、`'dataMarker'`、`'dataRegion'`、`''regionFilter'`、`'shape'`、`'html'`

  - **position** *dict*或*list*型

    当前标注位置：

    - 当传入字典时，用于定义对应图表相关字段键值对数据的位置，如`{ 'time': '2010-01-01', 'value': 200 }`

    - 当传入数组时，格式如`[x, y]`，其中`x`、`y`可以是图表坐标系中对应的数据值，百分比字符串如`'30%'`，或特殊位置关键词如`'min'`、`'max'`、`'median'`、`'start'`、`'end'`

  - **top** *bool*型，默认值：`False`

    是否将当前标注绘制到画布顶层

  - **offsetX** *int*或*float*型

    当前标注水平像素偏移量

  - **offsetY** *int*或*float*型

    当前标注竖直像素偏移量

  - **start** *list*型

    适用于`'line'`、`'region'`类型标注，设置作用范围起始位置

  - **end** *list*型

    适用于`'line'`、`'region'`类型标注，设置作用范围结束位置

  - **style** *dict*型

    当前标注样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **src** *str*型

    适用于`'image'`类型标注，设置图片地址

  - **content** *str*型

    适用于`'text'`类型标注，设置文本内容

  - **rotate** *int*或*float*型

    适用于`'text'`类型标注，设置文本旋转角度

  - **maxLength** *int*或*float*型

    适用于`'text'`类型标注，设置文本内容的最大像素长度

  - **autoEllipsis** *bool*型

    适用于`'text'`类型标注，设置文本内容超出`maxLength`限制时，是否自动省略

  - **ellipsisPosition** *str*型

    适用于`'text'`类型标注，设置文本内容超长省略截断的位置，可选项有`'head'`、`'middle'`、`'tail'`

  - **isVertical** *bool*型

    适用于`'text'`类型标注，针对直角坐标系，设置文本是否垂直显示

  - **background** *dict*型

    适用于`'text'`类型标注，配置文本背景框，支持的键值对属性有：

    - **style** *dict*型

      文本背景框样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **padding** *int*、*float*或*list*型

      文本背景框像素内边距

  - **color** *str*型

    适用于`'regionFilter'`类型标注，设置着色颜色

  - **apply** *list*型

    适用于`'regionFilter'`类型标注，设置区域着色只针对特定的矢量类型起作用

  - **autoAdjust** *bool*型

    适用于`'text'`类型标注，当文本超出绘图区域范围时，是否自动调整文本角度来适应绘图范围

  - **direction** *str*型

    当前标注朝向，可选项有`'upward'`、`'downward'`

  - **lineLength** *int*或*float*型

    适用于`'dataRegion'`类型标注，设置线像素长度

  - **container** *str*型

    自定义标记容器html源码字符串

  - **html** *str*或*dict*型

    适用于`'html'`类型标注，设置标注元素的html源码，支持传入`javascript`函数，通过`'func'`字段传入

  - **alignX** *str*型

    适用于`'html'`类型标注，设置标注元素水平方向对齐方式，可选项有`'left'`、`'middle'`、`'right'`

  - **alignY** *str*型

    适用于`'html'`类型标注，设置标注元素垂直方向对齐方式，可选项有`'top'`、`'middle'`、`'bottom'`