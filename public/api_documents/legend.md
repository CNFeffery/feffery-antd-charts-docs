- **<placeholder>** 

  *dict*或*bool*型，配置图例相关参数，设置为`False`时隐藏图例，支持的键值对属性有：

  - **position** *str*型

    图例位置，可选项有`'top'`、`'top-left'`、`'top-right'`、`'left'`、`'left-top'`、`'left-bottom'`、`'right'`、`'right-top'`、`'right-bottom'`、`'bottom'`、`'bottom-left'`、`'bottom-right'`

  - **layout** *str*型

    图例布局方式，可选项有`'horizontal'`、`'vertical'`

  - **radio** *bool*型，默认值：`True`

    是否启用图例交互指示器

  - **title** *dict*型
  
    配置图例标题，支持的键值对属性有：

    - **text** *str*型

      图例标题内容

    - **spacing** *int*或*float*型

      图例与图例项之间的像素间距

    - **style** *dict*型

      图例文字样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **offsetX** *int*或*float*型*

    图例整体在水平方向上的像素偏移

  - **offsetY** *int*或*float*型*

    图例整体在垂直方向上的像素偏移

  - **background** *dict*型
  
    配置图例背景，支持的键值对属性有：

    - **padding** *int*、*float*或*list*型

      图例背景框像素内边距

  - **flipPage** *bool*型

    针对分类型图例，是否在图例项较多时分页

  - **maxWidth** *int*或*float*型

    针对分类型图例，设置图例整体最大像素宽度

  - **maxHeight** *int*或*float*型

    针对分类型图例，设置图例整体最大像素高度

  - **reversed** *bool*型

    针对分类型图例，是否反转图例项顺序

  - **itemHeight** *int*或*float*型

    针对分类型图例，设置图例项像素高度

  - **itemWidth** *int*或*float*型

    针对分类型图例，设置图例项像素宽度

  - **itemName** *dict*型
  
    配置图例项名称，支持的键值对属性有：

    - **spacing** *int*或*float*型

      图例项名称与标记之间的像素间距

    - **style** *dict*型

      图例项名称样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **formatter** *dict*型

      图例项名称内容`javascript`格式化函数，通过`'func'`字段传入

  - **itemValue** *dict*型
  
    配置图例项数值，支持的键值对属性有：

    - **alignRight** *bool*型

      设置图例项宽度后，控制数值是否右对齐

    - **style** *dict*型

      图例项数值样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **formatter** *dict*型

      图例项数值内容`javascript`格式化函数，通过`'func'`字段传入

  - **itemSpacing** *int*或*float*型

    图例项水平像素间距

  - **selected** *dict*型

    自定义图例项高亮状态，格式如`{ 'item1': true, 'item2': false, 'item3': false }`

  - **min** *int*或*float*型

    针对连续型图例，设置图例选择范围的最小值

  - **max** *int*或*float*型

    针对连续型图例，设置图例选择范围的最大值

  - **value** *int*或*float*型

    针对连续型图例，设置图例当前停留位置对应的值

  - **slidable** *bool*型

    针对连续型图例，设置图例滑块是否可滑动

  - **rail** *dict*型
  
    配置连续型图例滑轨，支持的键值对属性有：

    - **type** *str*型

      滑轨类型，可选项有`'color'`、`'size'`

    - **size** *int*或*float*型

      滑轨像素宽度

    - **defaultLength** *int*或*float*型

      滑轨默认像素长度

    - **style** *dict*型

      滑轨样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **track** *dict*型

    配置连续型图例轨道，支持的键值对属性有：

    - **style** *dict*型

      滑轨选择范围样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **handler** *dict*型

    针对连续型图例，配置滑轨滑块，支持的键值对属性有：

    - **size** *int*或*float*型

      滑块像素尺寸

    - **style** *dict*型

      滑块样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **custom** *bool*型，默认值：`False`

    是否启用自定义图例模式，开启后需配合`items`参数进行自定义图例的定义

  - **items** *list*型

    自定义图例项，每个图例项为字典，支持的键值对属性有：

    - **name** *str*型

      当前图例项名称

    - **value** *int*或*float*型

      当前图例项数值

    - **marker** *dict*型

      配置当前图例项标记，支持的键值对属性有：

      - **symbol** *str*型

        图例项标记类型，可选项有`'circle'`、`'square'`、`'line'`、`'diamond'`、`'triangle'`、`'triangle-down'`、`'hexagon'`、`'bowtie'`、`'cross'`、`'tick'`、`'plus'`、`'hyphen'`

      - **style** *dict*型

        图例项标记样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

      - **spacing** *int*或*float*型

        图例项名称与标记之间的像素间距