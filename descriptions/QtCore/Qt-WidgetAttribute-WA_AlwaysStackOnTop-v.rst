.. sip:enum-member-description::
    :status: todo
    :value: 128
    :digest: 5b2d84e0766e9c34f1eed2ef2254cf8e

Since Qt 5.4, this value forces QOpenGLWidget and QQuickWidget to be drawn last, on top of other widgets. Ignored for other type of widgets. Setting this attribute breaks the stacking order, but allows having a semi-transparent OpenGL widget with other widgets visible underneath. It is strongly recommended to call update() on the widget's top-level window after enabling or disabling this attribute.
