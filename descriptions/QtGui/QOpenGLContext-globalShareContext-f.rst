.. sip:method-description::
    :status: todo
    :pysig: 7fe694e1683563ddccb2ed4fea1dfa63
    :realsig: ()
    :digest: c1a3c45272f9cd6dda60211bf5fa8c13

Returns the application-wide shared OpenGL context, if present. Otherwise, returns ``nullptr``.

This is useful if you need to upload OpenGL objects (buffers, textures, etc.) before creating or showing a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` or :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`.

**Warning:** Do not attempt to make the context returned by this function current on any surface. Instead, you can create a new context which shares with the global one, and then make the new context current.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts`, :sip:ref:`~PyQt6.QtGui.QOpenGLContext.setShareContext`, :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent`.
