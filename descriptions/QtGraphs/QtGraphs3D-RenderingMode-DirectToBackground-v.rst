.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: d7f8ae460ae2f2acbf10c8bf48d58198

Indicates that the graph will be rendered directly on the window background and QML items are rendered on top of it. Using non-transparent QML item as a background will hide the graph. Clears the whole window before rendering the graph, including the areas outside the graph. If the surface format of the window supports antialiasing, it will be used (see QQuick3D::idealSurfaceFormat()). This rendering mode offers the best performance at the expense of non-standard QML behavior. For example, the graphs do not obey the z ordering of QML items and the opacity value has no effect on them.
