.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 35ae8d20d5f11f0a38b9de85d1d208fb

This virtual function is called whenever the widget has been resized. Reimplement it in a subclass. The new size is passed in *w* and *h*.

There is no need to call :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.makeCurrent` because this has already been done when this function is called. Additionally, the framebuffer is also bound.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.initializeGL`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.paintGL`.
