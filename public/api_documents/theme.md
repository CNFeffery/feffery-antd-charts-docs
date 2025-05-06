- **<placeholder>** 

  *dict*或*str*型，配置图表主题，可设置`'default'`或`'dark'`使用内置主题，也可传入字典自行配置主题，支持的键值对属性有：

  - **background** *str*型

    画布背景色

  - **colors10** *list*型

    分类颜色数组，分类个数小于`10`时使用

  - **colors20** *list*型

    分类颜色数组，分类个数大于`10`时使用
  
  - **styleSheet** *dict*型

    自定义主题样式，可用的键值对属性有：

    - **backgroundColor** *str*型

      画布背景色

    - **paletteQualitative10** *list*型

      分类颜色数组，分类个数小于`10`时使用

    - **paletteQualitative20** *list*型

      分类颜色数组，分类个数大于`10`时使用

    - **fontFamily** *str*型

      文字字体

  - **withTheme** *str*型

    设置需要融合的内置主题类型，可选项有`'default'`、`'dark'`

  - **components** *dict*型

    为坐标轴、图例等图表构件配置主题样式