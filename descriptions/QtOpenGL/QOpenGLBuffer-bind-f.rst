.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: bbabc6d44f5814b592ffc612cffe3a6e

Binds the buffer associated with this object to the current OpenGL context. Returns ``false`` if binding was not possible, usually because :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.type` is not supported on this OpenGL implementation.

The buffer must be bound to the same `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ current when :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create` was called, or to another `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ that is sharing with it. Otherwise, false will be returned from this function.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.release`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create`.
