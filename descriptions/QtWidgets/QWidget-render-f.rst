.. sip:method-description::
    :status: todo
    :pysig: fb15fff4590d6fe7ba294e27399ddf10
    :realsig: (QPaintDevice*,const QPoint&,const QRegion&,QWidget::RenderFlags)
    :digest: 5b4962ea9ff9774bdadd4b33ee7c17b8

Renders the *sourceRegion* of this widget into the *target* using *renderFlags* to determine how to render. Rendering starts at *targetOffset* in the *target*. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 93-94

If *sourceRegion* is a null region, this function will use :sip:ref:`~PyQt6.QtWidgets.QWidget.rect` as the region, i.e. the entire widget.

Ensure that you call :sip:ref:`~PyQt6.QtGui.QPainter.end` for the *target* device's active painter (if any) before rendering. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 99-102

**Note:** To obtain the contents of a QOpenGLWidget, use QOpenGLWidget::grabFramebuffer() instead.
