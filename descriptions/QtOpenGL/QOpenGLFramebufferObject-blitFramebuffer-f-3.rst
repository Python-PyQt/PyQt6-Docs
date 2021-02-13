.. sip:method-description::
    :status: todo
    :pysig: f8cdbdd94491322ad75b02212f105698
    :realsig: (QOpenGLFramebufferObject*,const QRect&,QOpenGLFramebufferObject*,const QRect&,GLbitfield,GLenum,int,int,QOpenGLFramebufferObject::FramebufferRestorePolicy)
    :digest: 02b0718c4ec337306b6ca2e8a7ec2817

Blits from the *sourceRect* rectangle in the *source* framebuffer object to the *targetRect* rectangle in the *target* framebuffer object.

If *source* or *target* is 0, the default framebuffer will be used instead of a framebuffer object as source or target respectively.

This function will have no effect unless :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.hasOpenGLFramebufferBlit` returns true.

The *buffers* parameter should be a mask consisting of any combination of ``GL_COLOR_BUFFER_BIT``, ``GL_DEPTH_BUFFER_BIT``, and ``GL_STENCIL_BUFFER_BIT``. Any buffer type that is not present both in the source and target buffers is ignored.

The *sourceRect* and *targetRect* rectangles may have different sizes; in this case *buffers* should not contain ``GL_DEPTH_BUFFER_BIT`` or ``GL_STENCIL_BUFFER_BIT``. The *filter* parameter should be set to ``GL_LINEAR`` or ``GL_NEAREST``, and specifies whether linear or nearest interpolation should be used when scaling is performed.

If *source* equals *target* a copy is performed within the same buffer. Results are undefined if the source and target rectangles overlap and have different sizes. The sizes must also be the same if any of the framebuffer objects are multisample framebuffers.

**Note:** The scissor test will restrict the blit area if enabled.

When multiple render targets are in use, *readColorAttachmentIndex* and *drawColorAttachmentIndex* specify the index of the color attachments in the source and destination framebuffers.

The *restorePolicy* determines if the framebuffer that was bound prior to calling this function should be restored, or if the default framebuffer should be bound before returning, of if the caller is responsible for tracking and setting the bound framebuffer. Restoring the previous framebuffer can be relatively expensive due to the call to ``glGetIntegerv`` which on some OpenGL drivers may imply a pipeline stall.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.hasOpenGLFramebufferBlit`.
