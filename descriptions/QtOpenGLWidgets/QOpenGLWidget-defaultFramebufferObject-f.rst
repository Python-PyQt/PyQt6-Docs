.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 15e08aca564d7a331774a9b1b17be1aa

Returns The framebuffer object handle or ``0`` if not yet initialized.

**Note:** The framebuffer object belongs to the context returned by :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context` and may not be accessible from other contexts.

**Note:** The context and the framebuffer object used by the widget changes when reparenting the widget via setParent(). In addition, the framebuffer object changes on each resize.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.context`.
