- **<placeholder>** 

  *dict*或*bool*型，配置信息框相关参数，设置为`False`时不显示，支持的键值对属性有：

  - **fields** *list*型

    需要在信息框中显示的字段

  - **formatter** *dict*型

    信息框内容`javascript`格式化函数，通过`'func'`字段传入

  - **follow** *bool*型，默认值：`True`

    信息框是否跟随鼠标移动

  - **enterable** *bool*型，默认值：`False`

    信息框是否允许鼠标移入

  - **showTitle** *bool*型，默认值：`False`

    是否显示信息框标题

  - **title** *str*型

    控制信息框标题，传入有效字段名时会显示对应字段值，否则则直接显示传入的标题文本

  - **position** *str*型

    信息框相对于数据点的位置，可选项有`'top'`、`'bottom'`、`'left'`、`'right'`

  - **showMarkers** *bool*型，默认值：`True`

    信息框内是否显示各项图形标记

  - **marker** *dict*型

    信息框各项图形标记样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **domStyles** *dict*型

    分别控制信息框中不同构成部分的css样式，具体的构成部分对应键有`'g2-tooltip'`、`'g2-tooltip-title'`、`'g2-tooltip-list'`、`'g2-tooltip-list-item'`、`'g2-tooltip-marker'`、`'g2-tooltip-value'`、`'g2-tooltip-name'`

  - **offset** *int*或*float*型

    信息框像素偏移量

  - **reversed** *bool*型

    是否翻转显示信息框中的各子项

  - **showNil** *bool*型

    是否显示信息框中数值为空的子项

  - **customItems** *dict*型

    信息框子项`javascript`预处理函数，通过`'func'`字段传入

  - **shared** *bool*型

    是否合并展示当前数据点对应的所有数据
