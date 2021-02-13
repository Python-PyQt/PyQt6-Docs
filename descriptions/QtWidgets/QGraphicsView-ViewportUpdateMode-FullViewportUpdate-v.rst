.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: db869a32e8f53dfd4446e975ec664b00

When any visible part of the scene changes or is reexposed, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` will update the entire viewport. This approach is fastest when :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` spends more time figuring out what to draw than it would spend drawing (e.g., when very many small items are repeatedly updated). This is the preferred update mode for viewports that do not support partial updates, such as :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, and for viewports that need to disable scroll optimization.
