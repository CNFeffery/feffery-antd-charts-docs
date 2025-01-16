- **<placeholder>** 

  *dict*型，配置折线相关参数，支持的键值对属性有：

  - **func** *str*型

    定义动态返回贴图配置项参数对象的`javascript`函数体字符串

  - **type** *str*型

    贴图类型，可选项有`'dot'`、`'square'`、`'line'`

  - **cfg** *dict*型

    配置贴图样式，支持的键值对属性有：

    - **backgroundColor** *str*型

      贴图背景色

    - **fill** *str*型

      贴图元素填充色

    - **fillOpacity** *int*或*float*型

      贴图元素填充透明度，取值应在`0`到`1`之间

    - **stroke** *str*型

      贴图元素描边色

    - **strokeOpacity** *int*或*float*型

      贴图元素填充透明度，取值应在`0`到`1`之间

    - **lineWidth** *int*或*float*型

      贴图元素描边像素宽度

    - **opacity** *int*或*float*型

      贴图整体透明度，取值应在`0`到`1`之间

    - **rotation** *int*或*float*型

      贴图整体旋转角度

    - **size** *int*或*float*型，默认值：`6`

      适用于`'dot'`、`'square'`类型贴图，设置圆点或矩形像素大小

    - **padding** *int*或*number*型

      适用于`'dot'`、`'square'`类型贴图，设置圆点或矩形之间的像素间隔大小

    - **spacing** *int*或*float*型，默认值：`5`

      适用于`'line'`类型贴图，设置线条之间的像素距离

    - **isStagger** *bool*型，默认值：`True`

      适用于`'dot'`、`'square'`类型贴图，控制圆点或矩形之间是否交错