.. sip:method-description::
    :status: todo
    :pysig: 1e779733de9e0bad8d4591892ce7b4c9
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: 65fb1e1f23ad5cdb4e6dd4af0dfb88b3

Creates a new :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` for *widget*, adds it to the scene, and returns a pointer to the proxy. *wFlags* set the default window flags for the embedding proxy widget.

The item's position is initialized to (0, 0).

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``true``), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

Note that widgets with the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_PaintOnScreen` widget attribute set and widgets that wrap an external application or controller are not supported. Examples are :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget` and :sip:ref:`~PyQt6.QAxContainer.QAxWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addSimpleText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`.
