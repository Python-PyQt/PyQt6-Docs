.. sip:method-description::
    :status: todo
    :pysig: dc6b9a40201e9833cab35f988d477db0
    :realsig: () const
    :digest: 4057ef82daa21587b7d955302beed4a9

Returns The `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ used by this widget or ``0`` if not yet initialized.

**Note:** The context and the framebuffer object used by the widget changes when reparenting the widget via setParent().

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOpenGLContext.setShareContext`, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.defaultFramebufferObject`.
