- **<placeholder>** 

  *dict*型，配置刷选功能相关参数，支持的键值对属性有：

  - **enabled** *bool*型，默认值：`False`

    是否启用刷选功能

  - **type** *str*型，默认值：`'rect'`

    刷选类型，可选项有`'rect'`、`'x-rect'`、`'y-rect'`、`'circle'`、`'path'`

  - **action** *str*型，默认值：`'filter'`

    刷选动作类型，可选项有`'filter'`、`'highlight'`

  - **mask** *dict*型

    刷选范围样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **button** *dict*型

    配置刷选重置按钮，支持的键值对属性有：

    - **padding** *int*、*float*或*list*型

      按钮像素内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组

    - **text** *str*型

      按钮文本内容

    - **textStyle** *dict*型

      按钮文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **buttonStyle** *dict*型

      配置按钮样式，支持的键值对属性有:

      - **default** *dict*型

        按钮默认状态样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

      - **active** *dict*型

        按钮激活状态样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
