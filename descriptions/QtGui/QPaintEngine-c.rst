.. sip:class-description::
    :status: todo
    :brief: Abstract definition of how QPainter draws to a given device on a given platform
    :digest: 64806b0ddb9da42510e1e882ea5b4c3b

The :sip:ref:`~PyQt6.QtGui.QPaintEngine` class provides an abstract definition of how :sip:ref:`~PyQt6.QtGui.QPainter` draws to a given device on a given platform.

Qt provides several premade implementations of :sip:ref:`~PyQt6.QtGui.QPaintEngine` for the different painter backends we support. The primary paint engine provided is the raster paint engine, which contains a software rasterizer which supports the full feature set on all supported platforms. This is the default for painting on `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_-based classes in e.g. on Windows, X11 and macOS, it is the backend for painting on :sip:ref:`~PyQt6.QtGui.QImage` and it is used as a fallback for paint engines that do not support a certain capability. In addition we provide :sip:ref:`~PyQt6.QtGui.QPaintEngine` implementations for OpenGL (accessible through :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`) and printing (which allows using :sip:ref:`~PyQt6.QtGui.QPainter` to draw on a :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` object).

If one wants to use :sip:ref:`~PyQt6.QtGui.QPainter` to draw to a different backend, one must subclass :sip:ref:`~PyQt6.QtGui.QPaintEngine` and reimplement all its virtual functions. The :sip:ref:`~PyQt6.QtGui.QPaintEngine` implementation is then made available by subclassing :sip:ref:`~PyQt6.QtGui.QPaintDevice` and reimplementing the virtual function :sip:ref:`~PyQt6.QtGui.QPaintDevice.paintEngine`.

:sip:ref:`~PyQt6.QtGui.QPaintEngine` is created and owned by the :sip:ref:`~PyQt6.QtGui.QPaintDevice` that created it.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter`, :sip:ref:`~PyQt6.QtGui.QPaintDevice.paintEngine`, `Paint System <https://doc.qt.io/qt-6/paintsystem.html>`_.
