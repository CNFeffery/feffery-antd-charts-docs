- **<placeholder>** 

  *list*型，分别定义左轴、右轴配置项，格式为`[左轴配置项，右轴配置项]`，轴配置项为*dict*型，不同轴类型支持的键值对属性有：

  - 折线图类型

    - **geometry** *str*型

      当前轴图表类型，可选项为`'line'`（折线图）、`'column'`（柱状图）

    - **seriesField** *str*型

      同[AntdLine](/AntdLine)组件的同名参数

    - **smooth** *bool*型，默认值：`False`

      同[AntdLine](/AntdLine)组件的同名参数

    - **connectNulls** *bool*型，默认值：`True`

      同[AntdLine](/AntdLine)组件的同名参数

    - **lineStyle** *dict*型

      同[AntdLine](/AntdLine)组件的同名参数

    - **point** *dict*型

      同[AntdLine](/AntdLine)组件的同名参数

    - **label** *dict*型

      同[AntdLine](/AntdLine)组件的同名参数

    - **color** *str*、*list*或*dict*型

      同[AntdLine](/AntdLine)组件的同名参数

    - **stepType** *str*型

      同[AntdLine](/AntdLine)组件的同名参数

  - 柱状图类型

    - **geometry** *str*型

      当前轴图表类型，可选项为`'line'`（折线图）、`'column'`（柱状图）

    - **seriesField** *str*型

      同[AntdColumn](/AntdColumn)组件的同名参数

    - **groupField** *str*型

      同[AntdColumn](/AntdColumn)组件的同名参数

    - **isGroup** *bool*型

      同[AntdColumn](/AntdColumn)组件的同名参数

    - **isStack** *bool*型

      同[AntdColumn](/AntdColumn)组件的同名参数

    - **columnWidthRatio** *int*或*float*型

      同[AntdColumn](/AntdColumn)组件的同名参数

    - **marginRatio** *int*或*float*型

      同[AntdColumn](/AntdColumn)组件的同名参数

    - **columnStyle** *dict*型

      同[AntdColumn](/AntdColumn)组件的同名参数

    - **label** *dict*型

      同[AntdColumn](/AntdColumn)组件的同名参数
  
    - **color** *str*、*list*或*dict*型

      同[AntdColumn](/AntdColumn)组件的同名参数
