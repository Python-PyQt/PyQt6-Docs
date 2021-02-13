.. sip:class-description::
    :status: todo
    :brief: Convenience class for using QPainter on a QWindow
    :digest: 52ea7e92fbc06d18f9f18fce17cd2daf

:sip:ref:`~PyQt6.QtGui.QRasterWindow` is a convenience class for using :sip:ref:`~PyQt6.QtGui.QPainter` on a :sip:ref:`~PyQt6.QtGui.QWindow`.

:sip:ref:`~PyQt6.QtGui.QRasterWindow` is a :sip:ref:`~PyQt6.QtGui.QWindow` with a raster-based, non-OpenGL surface. On top of the functionality offered by :sip:ref:`~PyQt6.QtGui.QWindow`, :sip:ref:`~PyQt6.QtGui.QRasterWindow` adds a virtual paintEvent() function and the possibility to open a :sip:ref:`~PyQt6.QtGui.QPainter` on itself. The underlying paint engine will be the raster one, meaning that all drawing will happen on the CPU. For performing accelerated, OpenGL-based drawing, use QOpenGLWindow instead.

Internally the class is thin wrapper for :sip:ref:`~PyQt6.QtGui.QWindow` and :sip:ref:`~PyQt6.QtGui.QBackingStore` and is very similar to the `Raster Window Example <https://doc.qt.io/qt-6/qtgui-rasterwindow-example.html>`_ that uses these classes directly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintDeviceWindow.paintEvent`, :sip:ref:`~PyQt6.QtGui.QPaintDeviceWindow.update`.
