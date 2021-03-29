.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: (const QRect&)
    :digest: 3fb7955704e79aae03a737d3b5172fe7

Sets the painter's window to the given *rectangle*, and enables view transformations.

The window rectangle is part of the view transformation. The window specifies the logical coordinate system. Its sister, the :sip:ref:`~PyQt6.QtGui.QPainter.viewport`, specifies the device coordinate system.

The default window rectangle is the same as the device's rectangle.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.window`, :sip:ref:`~PyQt6.QtGui.QPainter.viewTransformEnabled`, `Window-Viewport Conversion <https://doc.qt.io/qt-6/coordsys.html#window-viewport-conversion>`_.
