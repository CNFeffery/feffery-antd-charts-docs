- **<placeholder>** 

  *dict*型，配置矩形树图下钻功能，支持的键值对属性有：

  - **enabled** *bool*型，默认值：`False`

    是否启用矩形树图下钻功能

  - **breadCrumb** *dict*型

    配置下钻层级引导交互面包屑控件，支持的键值对属性有：

    - **position** *str*型，默认值：`'bottom-left'`

      控件位置，可选项有`'top-left'`、`'bottom-left'`

    - **rootText** *str*型

      自定义根节点文案内容

    - **dividerText** *str*型，默认值：`/`

      自定义层级分隔文本内容

    - **textStyle** *dict*型

      文字样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **activeTextStyle** *dict*型

      鼠标移入状态文字样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
