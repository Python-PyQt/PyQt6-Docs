.. sip:method-description::
    :status: todo
    :pysig: 7a39468821742bb7c4d28ef08945d473
    :realsig: (QOpenGLTexture::TextureFormat)
    :digest: 5e1b3a8b6606390f22a3d507b01d43c7

Sets the format of this texture object to *format*. This function must be called before texture storage is allocated.

Note that all formats may not be supported. The exact set of supported formats is dependent upon your OpenGL implementation and version.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.format`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.allocateStorage`.
