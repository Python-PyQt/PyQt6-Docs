.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: 93303caea4010d6fc9ed44672850f732

When any visible part of the scene changes or is reexposed, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` will update the entire viewport. This approach is fastest when :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` spends more time figuring out what to draw than it would spend drawing (e.g., when very many small items are repeatedly updated). This is the preferred update mode for viewports that do not support partial updates, such as QOpenGLWidget, and for viewports that need to disable scroll optimization.
