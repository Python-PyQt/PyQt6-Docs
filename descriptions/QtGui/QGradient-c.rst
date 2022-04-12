.. sip:class-description::
    :status: todo
    :brief: Used in combination with QBrush to specify gradient fills
    :digest: aa72e03a216b8a642f1fbb74e2bd7162

The :sip:ref:`~PyQt6.QtGui.QGradient` class is used in combination with :sip:ref:`~PyQt6.QtGui.QBrush` to specify gradient fills.

Qt currently supports three types of gradient fills:

* *Linear* gradients interpolate colors between start and end points.

* *Simple* radial gradients interpolate colors between a focal point and end points on a circle surrounding it.

* *Extended* radial gradients interpolate colors between a center and a focal circle.

* *Conical* gradients interpolate colors around a center point.

A gradient's type can be retrieved using the :sip:ref:`~PyQt6.QtGui.QGradient.type` function. Each of the types is represented by a subclass of :sip:ref:`~PyQt6.QtGui.QGradient`:

+-----------------------------------------+-----------------------------------------+------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QLinearGradient` | :sip:ref:`~PyQt6.QtGui.QRadialGradient` | :sip:ref:`~PyQt6.QtGui.QConicalGradient` |
+=========================================+=========================================+==========================================+
| |image-qgradient-linear-png|            | |image-qgradient-radial-png|            | |image-qgradient-conical-png|            |
+-----------------------------------------+-----------------------------------------+------------------------------------------+

The colors in a gradient are defined using stop points of the QGradientStop type; i.e., a position and a color. Use the :sip:ref:`~PyQt6.QtGui.QGradient.setColorAt` function to define a single stop point. Alternatively, use the :sip:ref:`~PyQt6.QtGui.QGradient.setStops` function to define several stop points in one go. Note that the latter function *replaces* the current set of stop points.

It is the gradient's complete set of stop points (accessible through the :sip:ref:`~PyQt6.QtGui.QGradient.stops` function) that describes how the gradient area should be filled. If no stop points have been specified, a gradient of black at 0 to white at 1 is used.

A diagonal linear gradient from black at (100, 100) to white at (200, 200) could be specified like this:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-brush-brush.py
    :lines: 59-61

A gradient can have an arbitrary number of stop points. The following would create a radial gradient starting with red in the center, blue and then green on the edges:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-brush-brush.py
    :lines: 66-69

It is possible to repeat or reflect the gradient outside its area by specifying the :sip:ref:`~PyQt6.QtGui.QGradient.Spread` using the :sip:ref:`~PyQt6.QtGui.QGradient.setSpread` function. The default is to pad the outside area with the color at the closest stop point. The currently set :sip:ref:`~PyQt6.QtGui.QGradient.Spread` can be retrieved using the :sip:ref:`~PyQt6.QtGui.QGradient.spread` function. The :sip:ref:`~PyQt6.QtGui.QGradient.Spread` enum defines three different methods:

+----------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------+
| |image-qradialgradient-pad-png|                    | |image-qradialgradient-repeat-png|                    | |image-qradialgradient-reflect-png|                    |
+----------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QGradient.Spread.PadSpread` | :sip:ref:`~PyQt6.QtGui.QGradient.Spread.RepeatSpread` | :sip:ref:`~PyQt6.QtGui.QGradient.Spread.ReflectSpread` |
+----------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------+

Note that the :sip:ref:`~PyQt6.QtGui.QGradient.setSpread` function only has effect for linear and radial gradients. The reason is that the conical gradient is closed by definition, i.e. the *conical* gradient fills the entire circle from 0 - 360 degrees, while the boundary of a radial or a linear gradient can be specified through its radius or final stop points, respectively.

The gradient coordinates can be specified in logical coordinates, relative to device coordinates, or relative to object bounding box coordinates. The :sip:ref:`~PyQt6.QtGui.QGradient.CoordinateMode` can be set using the :sip:ref:`~PyQt6.QtGui.QGradient.setCoordinateMode` function. The default is :sip:ref:`~PyQt6.QtGui.QGradient.CoordinateMode.LogicalMode`, where the gradient coordinates are specified in the same way as the object coordinates. To retrieve the currently set :sip:ref:`~PyQt6.QtGui.QGradient.CoordinateMode` use :sip:ref:`~PyQt6.QtGui.QGradient.coordinateMode`.

.. seealso:: `The Gradients Example <https://doc.qt.io/qt-6/qtwidgets-painting-gradients-example.html>`_, :sip:ref:`~PyQt6.QtGui.QBrush`.

.. |image-qgradient-linear-png| image:: ../../../images/qgradient-linear.png
.. |image-qgradient-radial-png| image:: ../../../images/qgradient-radial.png
.. |image-qgradient-conical-png| image:: ../../../images/qgradient-conical.png
.. |image-qradialgradient-pad-png| image:: ../../../images/qradialgradient-pad.png
.. |image-qradialgradient-repeat-png| image:: ../../../images/qradialgradient-repeat.png
.. |image-qradialgradient-reflect-png| image:: ../../../images/qradialgradient-reflect.png
