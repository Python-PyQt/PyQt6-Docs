.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: f1bd3b9c71fd649090d84ad43fee3b09

Returns whether this texture uses a fixed pattern of multisample samples. If storage has not yet been allocated for this texture then this function returns the requested fixed sample position setting.

For texture targets that do not support multisampling this will return ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setFixedSamplePositions`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`.
