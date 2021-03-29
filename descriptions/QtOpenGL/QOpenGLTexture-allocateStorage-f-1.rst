.. sip:method-description::
    :status: todo
    :pysig: b10334629fa11b85429fd6109a327938
    :realsig: (QOpenGLTexture::PixelFormat,QOpenGLTexture::PixelType)
    :digest: 22ce52468e13b63cdefbc947fe217fb0

Allocates server-side storage for this texture object taking into account, the format, dimensions, mipmap levels, array layers and cubemap faces.

Once storage has been allocated it is no longer possible to change these properties.

If supported :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` makes use of immutable texture storage. However, if immutable texture storage is not available, then the specified *pixelFormat* and *pixelType* will be used to allocate mutable storage; note that in certain OpenGL implementations (notably, OpenGL ES 2) they must perfectly match the format and the type passed to any subsequent :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setData` call.

Once storage has been allocated for the texture then pixel data can be uploaded via one of the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setData` overloads.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setData`.
