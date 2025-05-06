- **<placeholder>** 

  *dict*或*bool*型，配置缩略轴，支持的键值对属性有：

  - **start** *int*或*float*型

    初始化范围起始比例位置，取值应在`0`到`1`之间

  - **end** *int*或*float*型

    初始化范围结束比例位置，取值应在`0`到`1`之间

  - **height** *int*或*float*型

    缩略轴像素高度

  - **backgroundStyle** *dict*型

    缩略轴背景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **foregroundStyle** *dict*型

    缩略轴前景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **handlerStyle** *dict*型

    配置缩略轴手柄，支持的键值对属性有：

    - **width** *int*或*float*型

      手柄像素宽度

    - **height** *int*或*float*型

      手柄像素高度

    - **fill** *str*型

      手柄填充色

    - **highLightFill** *str*型

      手柄鼠标移入高亮状态下的填充色

    - **stroke** *str*型

      手柄轮廓色

    - **opacity** *int*或*float*型
    
      手柄透明度

    - **radius** *int*或*float*型

      手柄圆角程度

    - **cursor** *str*型

      手柄鼠标移入高亮状态下的鼠标指针类型

  - **textStyle** *dict*型

    缩略轴文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **minLimit** *int*或*float*型

    滑动范围下限

  - **maxLimit** *int*或*float*型

    滑动范围上限

  - **formatter** *dict*型

    缩略轴文本`javascript`格式化函数，通过`'func'`字段传入

  - **trendCfg** *dict*型

    配置趋势线背景，支持的键值对属性有：

    - **data** *list*型

      趋势线数据，默认会自动生成

    - **smooth** *bool*型

      是否渲染光滑折线

    - **isArea** *bool*型

      是否渲染为填充面积图

    - **backgroundStyle** *dict*型

      背景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **lineStyle** *dict*型

      折线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

    - **areaStyle** *dict*型

      面积填充样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)