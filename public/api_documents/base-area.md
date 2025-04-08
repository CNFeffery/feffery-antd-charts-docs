- **<placeholder>** 

  *dict*型，配置面积填充相关参数，支持的键值对属性有：

  - **smooth** *bool*型，默认值：`False`

    面积填充轮廓是否渲染为平滑曲线

  - **color** *str*、*list*或*dict*型

    控制填充面积颜色，可传入单个颜色，一组颜色或具有`'func'`键值对的字典，其中`'func'`键值对值为动态返回颜色值的`javascript`函数体字符串

  - **style** *dict*型

    配置填充面积样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
