.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 22dd19a6806cf863b46a4b53a91acd72

Returns the number of multisample sample points for this texture. If storage has not yet been allocated for this texture then this function returns the requested number of samples.

For texture targets that do not support multisampling this will return 0.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setSamples`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`.
