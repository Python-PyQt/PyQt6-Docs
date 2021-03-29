.. sip:method-description::
    :status: todo
    :pysig: b53df27f41e7e1e87eded6e72ecfdeb9
    :realsig: () const
    :digest: f93768cbcdd0fa0e3ff89cf64ceb9e00

Returns the shape of this item as a :sip:ref:`~PyQt6.QtGui.QPainterPath` in local coordinates. The shape is used for many things, including collision detection, hit tests, and for the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` functions.

The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` to return a simple rectangular shape, but subclasses can reimplement this function to return a more accurate shape for non-rectangular items. For example, a round item may choose to return an elliptic shape for better collision detection. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 152-157

The outline of a shape can vary depending on the width and style of the pen used when drawing. If you want to include this outline in the item's shape, you can create a shape from the stroke using :sip:ref:`~PyQt6.QtGui.QPainterPathStroker`.

This function is called by the default implementations of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contains` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithPath`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contains`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.prepareGeometryChange`, :sip:ref:`~PyQt6.QtGui.QPainterPathStroker`.
