- **<placeholder>** 

  *dict*型，配置回归线相关参数，支持的键值对属性有：

  - **type** *str*型

    回归线类型，可选项有`'exp'`、`'linear'`、`'loess'`、`'log'`、`'poly'`、`'pow'`、`'quad'`

  - **style** *dict*型

    回归线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)

  - **algorithm** *dict*型

    自定义回归线映射算法`javascript`格式化函数，通过`'func'`字段传入

  - **top** *bool*型

    回归线是否置于顶层显示
