.. sip:class-description::
    :status: todo
    :brief: The base class of objects that can be painted on with QPainter
    :digest: efbf360adb4f848a9d14eeff8d3c7ca4

The :sip:ref:`~PyQt6.QtGui.QPaintDevice` class is the base class of objects that can be painted on with :sip:ref:`~PyQt6.QtGui.QPainter`.

A paint device is an abstraction of a two-dimensional space that can be drawn on using a :sip:ref:`~PyQt6.QtGui.QPainter`. Its default coordinate system has its origin located at the top-left position. X increases to the right and Y increases downwards. The unit is one pixel.

The drawing capabilities of :sip:ref:`~PyQt6.QtGui.QPaintDevice` are currently implemented by the `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, :sip:ref:`~PyQt6.QtGui.QImage`, :sip:ref:`~PyQt6.QtGui.QPixmap`, :sip:ref:`~PyQt6.QtGui.QPicture`, and :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` subclasses.

To implement support for a new backend, you must derive from :sip:ref:`~PyQt6.QtGui.QPaintDevice` and reimplement the virtual :sip:ref:`~PyQt6.QtGui.QPaintDevice.paintEngine` function to tell :sip:ref:`~PyQt6.QtGui.QPainter` which paint engine should be used to draw on this particular device. Note that you also must create a corresponding paint engine to be able to draw on the device, i.e derive from :sip:ref:`~PyQt6.QtGui.QPaintEngine` and reimplement its virtual functions.

**Warning:** Qt requires that a :sip:ref:`~PyQt6.QtGui.QGuiApplication` object exists before any paint devices can be created. Paint devices access window system resources, and these resources are not initialized before an application object is created.

The :sip:ref:`~PyQt6.QtGui.QPaintDevice` class provides several functions returning the various device metrics: The :sip:ref:`~PyQt6.QtGui.QPaintDevice.depth` function returns its bit depth (number of bit planes). The :sip:ref:`~PyQt6.QtGui.QPaintDevice.height` function returns its height in default coordinate system units (e.g. pixels for :sip:ref:`~PyQt6.QtGui.QPixmap` and `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_) while :sip:ref:`~PyQt6.QtGui.QPaintDevice.heightMM` returns the height of the device in millimeters. Similiarily, the :sip:ref:`~PyQt6.QtGui.QPaintDevice.width` and :sip:ref:`~PyQt6.QtGui.QPaintDevice.widthMM` functions return the width of the device in default coordinate system units and in millimeters, respectively. Alternatively, the protected :sip:ref:`~PyQt6.QtGui.QPaintDevice.metric` function can be used to retrieve the metric information by specifying the desired :sip:ref:`~PyQt6.QtGui.QPaintDevice.PaintDeviceMetric.PaintDeviceMetric` as argument.

The :sip:ref:`~PyQt6.QtGui.QPaintDevice.logicalDpiX` and :sip:ref:`~PyQt6.QtGui.QPaintDevice.logicalDpiY` functions return the horizontal and vertical resolution of the device in dots per inch. The :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiX` and :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiY` functions also return the resolution of the device in dots per inch, but note that if the logical and physical resolution differ, the corresponding :sip:ref:`~PyQt6.QtGui.QPaintEngine` must handle the mapping. Finally, the :sip:ref:`~PyQt6.QtGui.QPaintDevice.colorCount` function returns the number of different colors available for the paint device.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngine`, :sip:ref:`~PyQt6.QtGui.QPainter`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_, `Paint System <https://doc.qt.io/qt-6/paintsystem.html>`_.
