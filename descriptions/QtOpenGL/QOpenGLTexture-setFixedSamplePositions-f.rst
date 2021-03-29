.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: acf5cb60797e3f1d8a4610189d26f37c

Sets whether the sample positions and number of samples used with a multisample capable texture target to *fixed*. If set to ``true`` the sample positions and number of samples used are the same for all texels in the image and will not depend upon the image size or internal format. This function should be called before storage is allocated for the texture.

For targets that do not support multisampling this function has no effect.

The default value is ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isFixedSamplePositions`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isStorageAllocated`.
