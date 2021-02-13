.. sip:method-description::
    :status: todo
    :pysig: 4c5a6f8bd38bbaeb226cc0be1d14c76f
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: 1886633ca4932bee2d83070b02978a95

Creates a new :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` for *widget*, adds it to the scene, and returns a pointer to the proxy. *wFlags* set the default window flags for the embedding proxy widget.

The item's position is initialized to (0, 0).

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``true``), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

Note that widgets with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_PaintOnScreen` widget attribute set and widgets that wrap an external application or controller are not supported. Examples are QOpenGLWidget and QAxWidget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addSimpleText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`.
