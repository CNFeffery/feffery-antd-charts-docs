*dict*型

  配置坐标系，支持的键值对属性有：

  - **type** *str*型

    坐标系类型，可选项有`'cartesian'`（笛卡尔坐标系）、`'polar'`（极坐标系）、`'helix'`（螺旋坐标系）、`'theta'`（角度映射坐标系）

  - **cfg** *dict*型

    坐标系配置项，适用于极坐标系，支持的键值对属性有：

    - **startAngle** *int*或*float*型

      起始弧度

    - **endAngle** *int*或*float*型

      结束弧度

    - **radius** *int*或*float*型

      极坐标系半径，取值应在`0`到`1`之间

    - **innerRadius** *int*或*float*型

      极坐标系内半径，取值应在`0`到`1`之间
