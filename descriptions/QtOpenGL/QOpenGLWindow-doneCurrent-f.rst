.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1d6f7276f5e69dc2afed5ebaa41ab7d6

Releases the context.

It is not necessary to call this function in most cases, since the widget will make sure the context is bound and released properly when invoking :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.makeCurrent`.
