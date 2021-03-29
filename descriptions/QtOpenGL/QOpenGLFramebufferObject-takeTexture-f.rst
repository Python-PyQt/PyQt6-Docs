.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: b4b47921ab257551f55163bd64bacb09

Returns the texture id for the texture attached to this framebuffer object. The ownership of the texture is transferred to the caller.

If the framebuffer object is currently bound, an implicit :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.release` will be done. During the next call to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.bind` a new texture will be created.

If a multisample framebuffer object is used, then there is no texture and the return value from this function will be invalid. Similarly, incomplete framebuffer objects will also return 0.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.texture`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.bind`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.release`.
