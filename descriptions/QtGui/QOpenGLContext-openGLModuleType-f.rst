.. sip:method-description::
    :status: todo
    :pysig: 71fe51888b9a699dd7cbd2bafdf30ec5
    :realsig: ()
    :digest: b3f1e5a4ae60860bce045b55833f95ee

Returns the underlying OpenGL implementation type.

On platforms where the OpenGL implementation is not dynamically loaded, the return value is determined during compile time and never changes.

**Note:** A desktop OpenGL implementation may be capable of creating ES-compatible contexts too. Therefore in most cases it is more appropriate to check :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.renderableType` or use the convenience function :sip:ref:`~PyQt6.QtGui.QOpenGLContext.isOpenGLES`.

**Note:** This function requires that the :sip:ref:`~PyQt6.QtGui.QGuiApplication` instance is already created.
