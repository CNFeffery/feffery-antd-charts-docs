- **<placeholder>** 

  *dict*或*bool*型，配置水波图中心统计内容相关参数，设置为`False`时隐藏，支持的键值对属性有：

  - **title** *dict*或*bool*型

    配置统计数值标题，设置为`False`时不显示标题，支持的键值对属性有：

    - **style** *dict*型

      统计内容标题css样式

    - **content** *str*型

      配置统计内容标题文本

    - **formatter** *dict*型

      统计内容`javascript`格式化函数，通过`'func'`字段传入

    - **customHtml** *dict*型

      统计内容标题动态html渲染`javascript`函数，通过`'func'`字段传入

    - **rotate** *int*或*float*型

      标题旋转角度

    - **offsetX** *int*或*float*型

      标题水平像素偏移

    - **offsetY** *int*或*float*型

      标题竖直像素偏移

  - **content** *dict*或*bool*型

    配置统计内容，设置为`False`时不显示内容，支持的键值对属性有：

    - **style** *dict*型

      统计内容css样式

    - **content** *str*型

      配置统计内容文本

    - **formatter** *dict*型

      统计内容`javascript`格式化函数，通过`'func'`字段传入

    - **customHtml** *dict*型

      统计内容动态html渲染`javascript`函数，通过`'func'`字段传入

    - **rotate** *int*或*float*型

      内容旋转角度

    - **offsetX** *int*或*float*型

      内容水平像素偏移

    - **offsetY** *int*或*float*型

      内容竖直像素偏移