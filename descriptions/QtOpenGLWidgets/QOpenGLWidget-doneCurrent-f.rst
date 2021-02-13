.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d41aee70c6a2ae38da00a694a2f4f1cc

Releases the context.

It is not necessary to call this function in most cases, since the widget will make sure the context is bound and released properly when invoking :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`.
