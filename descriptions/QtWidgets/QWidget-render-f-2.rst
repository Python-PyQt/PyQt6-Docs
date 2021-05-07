.. sip:method-description::
    :status: todo
    :pysig: 39a508bf2802e76c162a5e51bba3148a
    :realsig: (QPaintDevice*,const QPoint&,const QRegion&,QWidget::RenderFlags)
    :digest: ce79c339c463911ea6aaf23bdba17a95

Renders the *sourceRegion* of this widget into the *target* using *renderFlags* to determine how to render. Rendering starts at *targetOffset* in the *target*. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 93-94

If *sourceRegion* is a null region, this function will use :sip:ref:`~PyQt6.QtWidgets.QWidget.rect` as the region, i.e. the entire widget.

Ensure that you call :sip:ref:`~PyQt6.QtGui.QPainter.end` for the *target* device's active painter (if any) before rendering. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qwidget.py
    :lines: 99-102

**Note:** To obtain the contents of a :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`, use :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget.grabFramebuffer` instead.
