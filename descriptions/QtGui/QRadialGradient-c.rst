.. sip:class-description::
    :status: todo
    :brief: Used in combination with QBrush to specify a radial gradient brush
    :digest: b0d0895552ee105729d1726f7ae25432

The :sip:ref:`~PyQt6.QtGui.QRadialGradient` class is used in combination with :sip:ref:`~PyQt6.QtGui.QBrush` to specify a radial gradient brush.

Qt supports both simple and extended radial gradients.

Simple radial gradients interpolate colors between a focal point and end points on a circle surrounding it. Extended radial gradients interpolate colors between a focal circle and a center circle. Points outside the cone defined by the two circles will be transparent. For simple radial gradients the focal point is adjusted to lie inside the center circle, whereas the focal point can have any position in an extended radial gradient.

Outside the end points the gradient is either padded, reflected or repeated depending on the currently set :sip:ref:`~PyQt6.QtGui.QGradient.Spread` method:

+--------------------------------------------------------------+--------------------------------------------------------+-------------------------------------------------------+
| |image-qradialgradient-pad-png|                              | |image-qradialgradient-reflect-png|                    | |image-qradialgradient-repeat-png|                    |
+--------------------------------------------------------------+--------------------------------------------------------+-------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QGradient.Spread.PadSpread` (default) | :sip:ref:`~PyQt6.QtGui.QGradient.Spread.ReflectSpread` | :sip:ref:`~PyQt6.QtGui.QGradient.Spread.RepeatSpread` |
+--------------------------------------------------------------+--------------------------------------------------------+-------------------------------------------------------+

The colors in a gradient is defined using stop points of the QGradientStop type, i.e. a position and a color. Use the :sip:ref:`~PyQt6.QtGui.QGradient.setColorAt` or the :sip:ref:`~PyQt6.QtGui.QGradient.setStops` function to define the stop points. It is the gradient's complete set of stop points that describes how the gradient area should be filled. If no stop points have been specified, a gradient of black at 0 to white at 1 is used.

In addition to the functions inherited from :sip:ref:`~PyQt6.QtGui.QGradient`, the :sip:ref:`~PyQt6.QtGui.QRadialGradient` class provides the :sip:ref:`~PyQt6.QtGui.QRadialGradient.center`, :sip:ref:`~PyQt6.QtGui.QRadialGradient.focalPoint` and :sip:ref:`~PyQt6.QtGui.QRadialGradient.radius` functions returning the gradient's center, focal point and radius respectively.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QLinearGradient`, :sip:ref:`~PyQt6.QtGui.QConicalGradient`.

.. |image-qradialgradient-pad-png| image:: ../../../images/qradialgradient-pad.png
.. |image-qradialgradient-reflect-png| image:: ../../../images/qradialgradient-reflect.png
.. |image-qradialgradient-repeat-png| image:: ../../../images/qradialgradient-repeat.png
