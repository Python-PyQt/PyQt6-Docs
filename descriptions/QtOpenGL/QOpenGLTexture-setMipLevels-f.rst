.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 1fb9543d8e86d3bb336708036c67ade2

For texture targets that support mipmaps, this function sets the requested number of mipmap *levels* to allocate storage for. This function should be called before storage is allocated for the texture.

If the texture target does not support mipmaps this function has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.mipLevels`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.maximumMipLevels`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`.
