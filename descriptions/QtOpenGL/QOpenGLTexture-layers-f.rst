.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 04123ee6b08af86fae2b9b1197cfa9b1

Returns the number of array layers for this texture. If storage has not yet been allocated for this texture then this function returns the requested number of array layers.

For texture targets that do not support array layers this will return 1.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setLayers`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`.
