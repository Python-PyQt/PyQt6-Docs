.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 43b8e646a07d38117263250898e7858b

Allocates server-side storage for this texture object taking into account, the format, dimensions, mipmap levels, array layers and cubemap faces.

Once storage has been allocated it is no longer possible to change these properties.

If supported :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` makes use of immutable texture storage.

Once storage has been allocated for the texture then pixel data can be uploaded via one of the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setData` overloads.

**Note:** If immutable texture storage is not available, then a default pixel format and pixel type will be used to create the mutable storage. You can use the other  overload to specify exactly the pixel format and the pixel type to use when allocating mutable storage; this is particulary useful under certain OpenGL ES implementations (notably, OpenGL ES 2), where the pixel format and the pixel type used at allocation time must perfectly match the format and the type passed to any subsequent :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setData` call.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setData`.
