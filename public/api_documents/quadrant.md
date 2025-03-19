- **<placeholder>** 

  *dict*型，配置象限相关参数，支持的键值对属性有：

  - **xBaseline** *int*或*float*型，默认值：`0`

    横轴基准分割线位置

  - **yBaseline** *int*或*float*型，默认值：`0`

    纵轴基准分割线位置

  - **lineStyle** *dict*型

    分割线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **regionStyle** *dict*或*list*型

    象限填充区域样式，支持传入格式如`[左上, 右上, 右下, 左下]`格式的参数分别配置四个象限的样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **labels** *list*型

    配置各象限文字标注，格式如`[左上, 右上, 右下, 左下]`，各配置项为字典，支持的键值对参数有：

    - **content** *str*型

      当前标注文字内容

    - **position** *list*型

      当前标注坐标位置，格式如`[x, y]`

    - **style** *dict*型

      当前标注样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)