.. sip:method-description::
    :status: todo
    :pysig: 64a1e5fb21bbbebf6c8e03fbd369c42e
    :realsig: (QGraphicsEffect*)
    :digest: 26aebe35511c6ed90cb0a0ad0f83fa3e

The setGraphicsEffect function is for setting the widget's graphics effect.

Sets *effect* as the widget's effect. If there already is an effect installed on this widget, :sip:ref:`~PyQt6.QtWidgets.QWidget` will delete the existing effect before installing the new *effect*.

If *effect* is the installed effect on a different widget, setGraphicsEffect() will remove the effect from the widget and install it on this widget.

:sip:ref:`~PyQt6.QtWidgets.QWidget` takes ownership of *effect*.

**Note:** This function will apply the effect on itself and all its children.

**Note:** Graphics effects are not supported for OpenGL-based widgets, such as QGLWidget, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` and :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.graphicsEffect`.
