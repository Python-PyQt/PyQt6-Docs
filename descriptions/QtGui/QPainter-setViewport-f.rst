.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: (const QRect&)
    :digest: 171a039cefa7148700db9e1ef7f41e4f

Sets the painter's viewport rectangle to the given *rectangle*, and enables view transformations.

The viewport rectangle is part of the view transformation. The viewport specifies the device coordinate system. Its sister, the :sip:ref:`~PyQt6.QtGui.QPainter.window`, specifies the logical coordinate system.

The default viewport rectangle is the same as the device's rectangle.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.viewport`, :sip:ref:`~PyQt6.QtGui.QPainter.viewTransformEnabled`, `Window-Viewport Conversion <https://doc.qt.io/qt-6/coordsys.html#window-viewport-conversion>`_.
