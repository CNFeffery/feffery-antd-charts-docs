- **<placeholder>** 

  *dict*或*bool*型，配置横坐标轴相关参数，设置为`False`时隐藏对应坐标轴，支持的键值对属性有：

  - **top** *bool*型，默认值为`False`

    是否将坐标轴渲染于画布顶层，从而避免部分图表坐标轴被图形遮挡

  - **range** *list*型

    坐标轴绘图范围，`[0, 1]`表示完整范围

  - **position** *str*型

    适用于直角坐标系，设置坐标轴方位，可选项有`'top'`、`'bottom'`、`'left'`、`'right'`

  - **title** *dict*型

    配置坐标轴标题，支持的键值对属性有：

    - **text** *str*型

      标题内容

    - **style** *dict*型

      标题文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **position** *str*型

      标题对齐方式，可选项有`'center'`、`'start'`、`'end'`

    - **offset** *int*或*float*型

      标题与坐标轴之间的像素间距

    - **spacing** *int*或*float*型

      标题与坐标轴标签之间的像素间距

    - **autoRotate** *bool*型

      是否开启自动旋转

  - **label** *dict*或*bool*型

    配置坐标轴标签，设置为`False`时隐藏，支持的键值对属性有：

    - **offset** *int*或*float*型

      像素偏移量

    - **offsetX** *int*或*float*型

      水平方向像素偏移量

    - **offsetY** *int*或*float*型

      竖直方向像素偏移量

    - **style** *dict*型

      标签文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **autoRotate** *bool*型

      是否开启自动旋转

    - **rotate** *int*或*float*型

      文本旋转角度

    - **labelEmit** *bool*型

      适用于极坐标系，设置文本是否按照角度放射状显示

    - **position** *str*型

      标签位置，可选项有`'top'`、`'bottom'`、`'middle'`、`''left'`、`'right'`

    - **formatter** *dict*型

      文字内容`javascript`格式化函数，通过`'func'`字段传入

    - **autoHide** *bool*型

      是否自动隐藏

  - **line** *dict*型

    配置坐标轴线，支持的键值对属性有：

    - **style** *dict*型

      坐标轴线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **grid** *dict*型

    配置坐标轴网格，支持的键值对属性有：

    - **line** *dict*型

      配置网格线，支持的键值对属性有：

      - **style** *dict*型

        网格线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

      - **type** *str*型

        网格线类型，可选项有`'line'`、`'circle'`

    - **alternateColor** *str*或*list*型

        网格之间的填充色，可设置单个颜色或一组颜色

    - **alignTick** *bool*型

        网格线是否与刻度线对齐，设置为`False`时会处于刻度线之间

    - **closed** *bool*型

        针对`'circle'`型网格线是否闭合

  - **tickLine** *dict*型

    配置坐标轴刻度线，支持的键值对属性有：

    - **style** *dict*型

      刻度线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **alignTick** *bool*型

      刻度线是否与刻度值对齐

    - **length** *int*或*float*型

      刻度线像素长度

  - **subTickLine** *dict*型

    配置坐标轴子刻度线，支持的键值对属性有：

    - **style** *dict*型

      子刻度线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **count** *int*型

      子刻度线数量

    - **length** *int*或*float*型

      子刻度线像素长度

  - **nice** *bool*型

    是否自动优化坐标轴

  - **min** *int*或*float*型

    坐标轴最小值

  - **max** *int*或*float*型

    坐标轴最大值

  - **minLimit** *int*或*float*型

    坐标轴范围下限

  - **maxLimit** *int*或*float*型

    坐标轴范围上限

  - **tickCount** *int*型

    期望的坐标轴刻度数量

  - **tickInterval** *int*或*float*型

    坐标轴刻度间隔值