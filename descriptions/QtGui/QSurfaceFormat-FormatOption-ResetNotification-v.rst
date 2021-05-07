.. sip:enum-member-description::
    :status: todo
    :value: 0x0008
    :digest: 6f3618973cd683ca0e9529119b1bb134

Enables notifications about resets of the OpenGL context. The status is then queryable via the context's :sip:ref:`~PyQt6.QtGui.QOpenGLContext.isValid` function. Note that not setting this flag does not guarantee that context state loss never occurs. Additionally, some implementations may choose to report context loss regardless of this flag. Platforms that support dynamically enabling the monitoring of the loss of context, such as, Windows with WGL, or Linux/X11 (xcb) with GLX, will monitor the status in every call to :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent`. See :sip:ref:`~PyQt6.QtGui.QOpenGLContext.isValid` for more information on this.
