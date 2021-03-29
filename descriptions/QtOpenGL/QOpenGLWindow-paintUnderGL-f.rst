.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8d73aa277ee415cfb793a47f86a63776

The virtual function is called before each invocation of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`.

When the update mode is set to ``NoPartialUpdate``, there is no difference between this function and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`, performing rendering in either of them leads to the same result.

The difference becomes significant when using ``PartialUpdateBlend``, where an extra framebuffer object is used. There, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` targets this additional framebuffer object, which preserves its contents, while  and :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintOverGL` target the default framebuffer, i.e. directly the window surface, the contents of which is lost after each displayed frame.

**Note:** Avoid relying on this function when the update behavior is ``PartialUpdateBlit``. This mode involves blitting the extra framebuffer used by :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL` onto the default framebuffer after each invocation of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`, thus overwriting all drawing generated in this function.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.paintOverGL`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow.UpdateBehavior.UpdateBehavior`.
