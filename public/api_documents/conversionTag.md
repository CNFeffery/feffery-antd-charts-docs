- **<placeholder>** 

  *dict*型，配置转化标签相关参数，支持的键值对属性有：

  - **size** *int*或*float*型

    转化率标签像素尺寸

  - **spacing** *int*或*float*型

    转化率标签与图表元素之间的像素间距

  - **offset** *int*或*float*型

    组件与坐标轴之间的像素距离

  - **arrow** *dict*或*bool*型

    配置转化率组件箭头样式，设置为`False`时不显示箭头，支持的键值对属性有：

    - **headSize** *int*或*float*型

      箭头像素尺寸

  - **text** *dict*或*bool*型

    配置转化率组件文本，设置为`False`时不显示文本，支持的键值对属性有：

    - **formatter** *dict*型

      自定义转化率计算`javascript`函数，通过`'func'`字段传入

    - **style** *dict*型

      转化率文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
