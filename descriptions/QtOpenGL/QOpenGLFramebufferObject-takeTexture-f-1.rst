.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int)
    :digest: d9e85d412dc96ba55dac8b310a1e19af

This is an overloaded function.

Returns the texture id for the texture attached to the color attachment of index *colorAttachmentIndex* of this framebuffer object. The ownership of the texture is transferred to the caller.

When *colorAttachmentIndex* is ``0``, the behavior is identical to the parameter-less variant of this function.

If the framebuffer object is currently bound, an implicit :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.release` will be done. During the next call to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.bind` a new texture will be created.

If a multisample framebuffer object is used, then there is no texture and the return value from this function will be invalid. Similarly, incomplete framebuffer objects will also return 0.
