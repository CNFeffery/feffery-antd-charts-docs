- **<placeholder>** 

  *list*型，配置若干种交互功能，每个标注项为字典，支持的键值对属性有：

  - **type** *str*型

    当前交互类型，常用项有`'active-region'`、`'element-active'`、`'element-selected'`、`'element-single-selected'`、`'element-highlight'`、`'element-highlight-by-x'`、·'element-highlight-by-color'·、`'legend-filter'`、`'legend-visible-filter'`、`'legend-active'`、`'legend-highlight'`、`'legend-highlight'`、`'element-list-highlight'`、`'pie-statistic-active'`等，[拓展阅读](https://g2-v4.antv.vision/zh/docs/api/general/interaction)

  - **cfg** *dict*型

    当前交互类型对应的配置参数，[拓展阅读](https://g2-v4.antv.vision/zh/docs/api/general/interaction)

  - **enable** *bool*型

    是否启用当前交互