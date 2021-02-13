.. sip:class-description::
    :status: todo
    :brief: Drawing area for QWindow
    :digest: a382c13e867843e4dc1d8d3fe5755d82

The :sip:ref:`~PyQt6.QtGui.QBackingStore` class provides a drawing area for :sip:ref:`~PyQt6.QtGui.QWindow`.

:sip:ref:`~PyQt6.QtGui.QBackingStore` enables the use of :sip:ref:`~PyQt6.QtGui.QPainter` to paint on a :sip:ref:`~PyQt6.QtGui.QWindow` with type RasterSurface. The other way of rendering to a :sip:ref:`~PyQt6.QtGui.QWindow` is through the use of OpenGL with `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_.

A :sip:ref:`~PyQt6.QtGui.QBackingStore` contains a buffered representation of the window contents, and thus supports partial updates by using :sip:ref:`~PyQt6.QtGui.QPainter` to only update a sub region of the window contents.

:sip:ref:`~PyQt6.QtGui.QBackingStore` might be used by an application that wants to use :sip:ref:`~PyQt6.QtGui.QPainter` without OpenGL acceleration and without the extra overhead of using the `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` UI stacks. For an example of how to use :sip:ref:`~PyQt6.QtGui.QBackingStore` see the `Raster Window Example <https://doc.qt.io/qt-6/qtgui-rasterwindow-example.html>`_.
