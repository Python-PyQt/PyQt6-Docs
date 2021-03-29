.. sip:method-description::
    :status: todo
    :pysig: e27247e5b452ce98dcfc93f19679f890
    :realsig: () const
    :digest: 8b0e4c1c4daa4944cf56f3bb4a993241

Returns this item's scene transformation matrix. This matrix can be used to map coordinates and geometrical shapes from this item's local coordinate system to the scene's coordinate system. To map coordinates from the scene, you must first invert the returned matrix.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 100-107

Unlike :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, which returns only an item's local transformation, this function includes the item's (and any parents') position, and all the transfomation properties.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scenePos`, `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_, :ref:`Transformations<qgraphicsitem-transformations>`.
