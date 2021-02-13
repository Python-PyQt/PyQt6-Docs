.. sip:method-description::
    :status: todo
    :pysig: 3e1bcf19403b6f462466c2967baf6c8c
    :realsig: (QOpenGLFramebufferObject*,const QRect&,QOpenGLFramebufferObject*,const QRect&,GLbitfield,GLenum,int,int)
    :digest: 18dc33151351d14b459669959532591e

This is an overloaded function.

Convenience overload to blit between two framebuffer objects and to restore the previous framebuffer binding. Equivalent to calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.blitFramebuffer`\ (target, targetRect, source, sourceRect, buffers, filter, readColorAttachmentIndex, drawColorAttachmentIndex, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.FramebufferRestorePolicy.RestoreFrameBufferBinding`).
