- **<placeholder>** 

  *dict*型，配置折点相关参数，支持的键值对属性有：

  - **color** *str*、*list*或*dict*型

    控制图表主要元素颜色，可传入单个颜色，一组颜色或具有`'func'`键值对的字典，其中`'func'`键值对值为动态返回颜色值的`javascript`函数体字符串

  - **shape** *str*或*dict*型

    控制折点形状，可选项有`'circle'`、`'square'`、`'bowtie'`、`'diamond'`、`'hexagon'`、`'triangle'`、`'triangle-down'`、`'hollow-circle'`、`'hollow-square'`、`'hollow-bowtie'`、`'hollow-diamond'`、`'hollow-hexagon'`、`'hollow-triangle'`、`'hollow-triangle-down'`、`'cross'`、`'tick'`、`'plus'`、`'hyphen'`、`'line'`，支持传入具有`'func'`键值对的字典，其中`'func'`键值对值为动态返回点形状的`javascript`函数体字符串

  - **style** *dict*型

    配置折点样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)