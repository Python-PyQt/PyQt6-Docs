.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: 9263849e3ae643313e53f4be345aac09

:sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` will discard the contents of the color buffer and the ancillary buffers after the :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` is rendered to screen. This is the same behavior that can be expected by calling :sip:ref:`~PyQt6.QtGui.QOpenGLContext.swapBuffers` with a default opengl enabled :sip:ref:`~PyQt6.QtGui.QWindow` as the argument.  can have some performance benefits on certain hardware architectures common in the mobile and embedded space when a framebuffer object is used as the rendering target. The framebuffer object is invalidated between frames with glDiscardFramebufferEXT if supported or a glClear. Please see the documentation of EXT_discard_framebuffer for more information: https://www.khronos.org/registry/gles/extensions/EXT/EXT_discard_framebuffer.txt
