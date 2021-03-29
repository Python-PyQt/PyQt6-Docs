.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 56c0f71644c96a29231eec370f7642bd

Binds this texture to the currently active texture unit ready for rendering. Note that you do not need to bind :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` objects in order to modify them as the implementation makes use of the EXT_direct_state_access extension where available and simulates it where it is not.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.release`.
