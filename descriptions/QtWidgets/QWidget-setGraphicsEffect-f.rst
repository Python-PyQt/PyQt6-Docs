.. sip:method-description::
    :status: todo
    :pysig: 64a1e5fb21bbbebf6c8e03fbd369c42e
    :realsig: (QGraphicsEffect*)
    :digest: 53ad4545ec602af44d2d800f6fe491f6

The  function is for setting the widget's graphics effect.

Sets *effect* as the widget's effect. If there already is an effect installed on this widget, `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ will delete the existing effect before installing the new *effect*.

If *effect* is the installed effect on a different widget,  will remove the effect from the widget and install it on this widget.

`QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ takes ownership of *effect*.

**Note:** This function will apply the effect on itself and all its children.

**Note:** Graphics effects are not supported for OpenGL-based widgets, such as QGLWidget, :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` and :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.graphicsEffect`.
