.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 08ed85610da6214f8d4d1ec4f0c9c4c1

Enables mipmapping if *enabled* is true; otherwise disables it.

Mipmapping is disabled by default.

If mipmapping is enabled, additional memory will be allocated for the mipmap levels. The mipmap levels can be updated by binding the texture and calling glGenerateMipmap(). Mipmapping cannot be enabled for multisampled framebuffer objects.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat.mipmap`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.texture`.
