- **<placeholder>** 

  *dict*或*bool*型，配置滚动条相关参数，设置为`False`时不开启滚动条，支持的键值对属性有：

  - **type** *str*型，默认值：`'horizontal'`

    滚动条类型，可选项有`'horizontal'`、`'vertical'`

  - **width** *int*或*float*型

    适用于`'vertical'`类型滚动条，设置滚动条像素宽度

  - **height** *int*或*float*型

    适用于`'horizontal'`类型滚动条，设置滚动条像素高度

  - **padding** *int*、*float*或*list*型

    滚动条像素内边距

  - **categorySize** *int*或*float*型

    对于`'horizontal'`类型滚动条，设置X轴每个分类字段的像素宽度；对于`'vertical'`类型滚动条，设置X轴每个分类字段的像素高度

  - **style** *dict*型

    配置滚动条样式，支持的键值对属性有：

    - **trackColor** *str*型

      滚动条滑道颜色

    - **thumbColor** *str*型

      滚动条滑块颜色

    - **thumbHighlightColor** *str*型

      滚动条滑块高亮颜色

    - **lineCap** *str*型

      滚动条滑道圆角类型，可选项有`'butt'`、`'round'`、`'square'`
