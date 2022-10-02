.. sip:enum-member-description::
    :status: todo
    :value: 128
    :digest: edbf637f78394979a4f2acca524bd2a0

Forces :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` and :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` to be drawn last, on top of other widgets. Ignored for other type of widgets. Setting this attribute breaks the stacking order, but allows having a semi-transparent OpenGL widget with other widgets visible underneath. It is strongly recommended to call update() on the widget's top-level window after enabling or disabling this attribute.
