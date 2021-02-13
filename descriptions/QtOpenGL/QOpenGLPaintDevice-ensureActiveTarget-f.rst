.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9c46546f6113637133dd296a4008ab6e

This virtual method is provided as a callback to allow re-binding a target frame buffer object or context when different :sip:ref:`~PyQt6.QtOpenGL.QOpenGLPaintDevice` instances are issuing draw calls alternately.

:sip:ref:`~PyQt6.QtGui.QPainter.beginNativePainting` will also trigger this method.

The default implementation does nothing.
