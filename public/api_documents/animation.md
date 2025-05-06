- **<placeholder>**

  *dict*或*bool*型，配置图表渲染动画，设置为`False`时关闭动画，通过键值对方式为不同的阶段配置动画效果，可用的阶段键名有`'appear'`（初次加载阶段）、`'enter'`（图表更新阶段）、`'update'`（仅数据更新阶段）、`'leave'`（旧数据覆盖销毁退场阶段），支持的键值对属性有：

  - **animation** *str*型

    动画效果类型，可选项有`'fade-in'`、`'fade-out'`、`'grow-in-x'`、`'grow-in-y'`、`'grow-in-xy'`、`'scale-in-x'`、`'scale-in-y'`、`'wave-in'`、`'zoom-in'`、`'zoom-out'`、`'path-in'`、`'position-update'`

  - **duration** *int*或*float*型

    动画持续时长，单位：毫秒

  - **delay** *int*或*float*型

    动画渲染开始延时时长，单位：毫秒
