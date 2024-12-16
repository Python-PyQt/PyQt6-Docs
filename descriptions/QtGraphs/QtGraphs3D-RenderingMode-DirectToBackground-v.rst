.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: d5b3fc73c093c76cb5635916c34d2e93

Indicates that the graph will be rendered directly on the window background and QML items are rendered on top of it. Using non-transparent QML item as a background will hide the graph. Clears the whole window before rendering the graph, including the areas outside the graph. If the surface format of the window supports antialiasing, it will be used (see ``qDefaultSurfaceFormat()``). This rendering mode offers the best performance at the expense of non-standard QML behavior. For example, the graphs do not obey the z ordering of QML items and the opacity value has no effect on them.
