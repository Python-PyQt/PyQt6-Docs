.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 7c5c6ef4840cfb0ec0ea5903030c054f

Sets the number of *samples* to allocate storage for when rendering to a multisample capable texture target. This function should be called before storage is allocated for the texture.

For targets that do not support multisampling this function has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.samples`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`.
