.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 8d3feb42dedfc6659a8ecf6c0a592faf

Indicates that the drawing performed in :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` does not cover the entire window. In this case an extra framebuffer object is created under the hood, and rendering performed in :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` will target this framebuffer. This framebuffer is then blitted onto the window surface's default framebuffer after each paint. This allows having :sip:ref:`~PyQt6.QtGui.QPainter`-based drawing code in :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` which only repaints a smaller area at a time, because, unlike , the previous content is preserved.
