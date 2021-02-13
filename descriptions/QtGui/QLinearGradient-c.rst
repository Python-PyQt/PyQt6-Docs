.. sip:class-description::
    :status: todo
    :brief: Used in combination with QBrush to specify a linear gradient brush
    :digest: b398fca0a18b7b9ee8e13a9dc71466d8

The :sip:ref:`~PyQt6.QtGui.QLinearGradient` class is used in combination with :sip:ref:`~PyQt6.QtGui.QBrush` to specify a linear gradient brush.

Linear gradients interpolate colors between start and end points. Outside these points the gradient is either padded, reflected or repeated depending on the currently set :sip:ref:`~PyQt6.QtGui.QGradient.Spread` method:

+--------------------------------------------------------------+--------------------------------------------------------+-------------------------------------------------------+
| |image-qlineargradient-pad-png|                              | |image-qlineargradient-reflect-png|                    | |image-qlineargradient-repeat-png|                    |
+--------------------------------------------------------------+--------------------------------------------------------+-------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QGradient.Spread.PadSpread` (default) | :sip:ref:`~PyQt6.QtGui.QGradient.Spread.ReflectSpread` | :sip:ref:`~PyQt6.QtGui.QGradient.Spread.RepeatSpread` |
+--------------------------------------------------------------+--------------------------------------------------------+-------------------------------------------------------+

The colors in a gradient is defined using stop points of the QGradientStop type, i.e. a position and a color. Use the :sip:ref:`~PyQt6.QtGui.QGradient.setColorAt` or the :sip:ref:`~PyQt6.QtGui.QGradient.setStops` function to define the stop points. It is the gradient's complete set of stop points that describes how the gradient area should be filled. If no stop points have been specified, a gradient of black at 0 to white at 1 is used.

In addition to the functions inherited from :sip:ref:`~PyQt6.QtGui.QGradient`, the :sip:ref:`~PyQt6.QtGui.QLinearGradient` class provides the :sip:ref:`~PyQt6.QtGui.QLinearGradient.finalStop` function which returns the final stop point of the gradient, and the :sip:ref:`~PyQt6.QtGui.QLinearGradient.start` function returning the start point of the gradient.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QRadialGradient`, :sip:ref:`~PyQt6.QtGui.QConicalGradient`.

.. |image-qlineargradient-pad-png| image:: ../../../images/qlineargradient-pad.png
.. |image-qlineargradient-reflect-png| image:: ../../../images/qlineargradient-reflect.png
.. |image-qlineargradient-repeat-png| image:: ../../../images/qlineargradient-repeat.png
