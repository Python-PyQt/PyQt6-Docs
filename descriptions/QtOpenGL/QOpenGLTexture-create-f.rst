.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 9ed8812aa826eee64b056177a01cd567

Creates the underlying OpenGL texture object. This requires a current valid OpenGL context. If the texture object already exists, this function does nothing.

Once the texture object is created you can obtain the object name from the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.textureId` function. This may be useful if you wish to make some raw OpenGL calls related to this texture.

Normally it should not be necessary to call this function directly as all functions that set properties of the texture object implicitly call  on your behalf.

Returns ``true`` if the creation succeeded, otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.destroy`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isCreated`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.textureId`.
