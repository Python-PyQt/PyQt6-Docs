.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 3f056366a06a25edb3d343701742f1cc

Sets the number of array *layers* to allocate storage for. This function should be called before storage is allocated for the texture.

For targets that do not support array layers this function has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.layers`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`.
