.. sip:method-description::
    :status: todo
    :pysig: 7fe694e1683563ddccb2ed4fea1dfa63
    :realsig: ()
    :digest: 354e454a23c543bc284014a79ae440d7

Returns the application-wide shared OpenGL context, if present. Otherwise, returns ``nullptr``.

This is useful if you need to upload OpenGL objects (buffers, textures, etc.) before creating or showing a QOpenGLWidget or QQuickWidget.

**Note:** You must set the :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts` flag on :sip:ref:`~PyQt6.QtGui.QGuiApplication` before creating the :sip:ref:`~PyQt6.QtGui.QGuiApplication` object, otherwise Qt may not create a global shared context.

**Warning:** Do not attempt to make the context returned by this function current on any surface. Instead, you can create a new context which shares with the global one, and then make the new context current.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_ShareOpenGLContexts`, :sip:ref:`~PyQt6.QtGui.QOpenGLContext.setShareContext`, :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent`.
