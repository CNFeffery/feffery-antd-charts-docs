- **<placeholder>** 

  *dict*型，用于字段元配置，键为对应`data`的相关字段，值为对应字段的配置字典，支持的键值对属性有：

  - **type** *str*型

    声明当前字段度量类型，可选项有`'cat'`（分类度量）、`'timeCat'`（时间分类度量）、`'linear'`（线性度量）、`'time'`（连续的时间度量）、`'log'`（对数度量）、`'pow'`（幂数度量）、`'quantize'`（分段度量）、`'quantile'`（等分度量）、`'identity'`（常量度量）

  - **alias** *str*型

    当前字段显示别名

  - **values** *list*型

    枚举当前字段下所有值

  - **formatter** *dict*型

    统一设置当前字段在坐标轴、图例、信息框中对应的文字内容`javascript`格式化函数，通过`'func'`字段传入

  - **range** *list*型，默认值：`[0, 1]`
  
    当前字段绘图值域比例范围

  - **min** *int*或*float*型

    当前字段值域下限，分类度量下无效

  - **max** *int*或*float*型

    当前字段值域上限，分类度量下无效

  - **minLimit** *int*或*float*型

    强制设置当前字段的值域最小值，会影响坐标轴刻度开始位置，分类度量下无效

  - **maxLimit** *int*或*float*型

    强制设置当前字段的值域最大值，会影响坐标轴刻度结束位置，分类度量下无效

  - **base** *int*或*float*型

    对数度量下有效，用于定义底数

  - **exponent** *int*或*float*型

    幂数度量下有效，用于定义指数

  - **nice** *bool*型

    是否自动优化坐标轴

  - **ticks** *list*型

    为当前字段手动设置坐标轴刻度值，优先级最高

  - **minTickInterval** *int*或*float*型

    线性度量下有效，为当前字段设置坐标轴刻度最小间隔

  - **tickCount** *int*型

    为当前字段设置坐标轴刻度数量

  - **maxTickCount** *int*型

    为当前字段设置坐标轴刻度最大数量

  - **showLast** *bool*型

    连续时间度量下有效，设置是否强制显示坐标轴刻度最后的时间刻度值