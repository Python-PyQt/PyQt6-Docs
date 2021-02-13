.. sip:class-description::
    :status: todo
    :brief: Used in combination with QBrush to specify a conical gradient brush
    :digest: a9b9ca425aa43e1eaf449d117d52bd56

The :sip:ref:`~PyQt6.QtGui.QConicalGradient` class is used in combination with :sip:ref:`~PyQt6.QtGui.QBrush` to specify a conical gradient brush.

Conical gradients interpolate interpolate colors counter-clockwise around a center point.

.. image:: ../../../images/qconicalgradient.png

The colors in a gradient is defined using stop points of the QGradientStop type, i.e. a position and a color. Use the :sip:ref:`~PyQt6.QtGui.QGradient.setColorAt` or the :sip:ref:`~PyQt6.QtGui.QGradient.setStops` function to define the stop points. It is the gradient's complete set of stop points that describes how the gradient area should be filled. If no stop points have been specified, a gradient of black at 0 to white at 1 is used.

In addition to the functions inherited from :sip:ref:`~PyQt6.QtGui.QGradient`, the :sip:ref:`~PyQt6.QtGui.QConicalGradient` class provides the :sip:ref:`~PyQt6.QtGui.QConicalGradient.angle` and :sip:ref:`~PyQt6.QtGui.QConicalGradient.center` functions returning the start angle and center of the gradient.

Note that the setSpread() function has no effect for conical gradients. The reason is that the conical gradient is closed by definition, i.e. the conical gradient fills the entire circle from 0 - 360 degrees, while the boundary of a radial or a linear gradient can be specified through its radius or final stop points, respectively.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QLinearGradient`, :sip:ref:`~PyQt6.QtGui.QRadialGradient`, `The Gradients Example <https://doc.qt.io/qt-6/qtwidgets-painting-gradients-example.html>`_.
