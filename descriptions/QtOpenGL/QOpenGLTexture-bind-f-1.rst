.. sip:method-description::
    :status: todo
    :pysig: 292b074c891d10503afdee86843a7a4b
    :realsig: (uint,QOpenGLTexture::TextureUnitReset)
    :digest: 7f52112f3aaad7ca8b152a8aa288e907

Binds this texture to texture unit *unit* ready for rendering. Note that you do not need to bind :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` objects in order to modify them as the implementation makes use of the EXT_direct_state_access extension where available and simulates it where it is not.

If parameter *reset* is ``true`` then this function will restore the active unit to the texture unit that was active upon entry.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.release`.
