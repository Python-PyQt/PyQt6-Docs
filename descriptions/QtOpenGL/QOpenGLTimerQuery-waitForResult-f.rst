.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: e4e0c16b656b74717a9c46b2f0bfee67

Returns the result of the OpenGL timer query.

This function will block until the result is made available by OpenGL. It is recommended to call :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.isResultAvailable` to ensure that the result is available to avoid unnecessary blocking and stalling.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTimerQuery.isResultAvailable`.
