.. sip:class-description::
    :status: todo
    :brief: Container that treats a group of items as a single item
    :digest: dba1e2b252237f32c59aefdf21fe816a

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup` class provides a container that treats a group of items as a single item.

A :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup` is a special type of compound item that treats itself and all its children as one item (i.e., all events and geometries for all children are merged together). It's common to use item groups in presentation tools, when the user wants to group several smaller items into one big item in order to simplify moving and copying of items.

If all you want is to store items inside other items, you can use any :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` directly by passing a suitable parent to setParentItem().

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.boundingRect` function of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup` returns the bounding rectangle of all items in the item group. :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup` ignores the ItemIgnoresTransformations flag on its children (i.e., with respect to the geometry of the group item, the children are treated as if they were transformable).

There are two ways to construct an item group. The easiest and most common approach is to pass a list of items (e.g., all selected items) to :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.createItemGroup`, which returns a new :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup` item. The other approach is to manually construct a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup` item, add it to the scene calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, and then add items to the group manually, one at a time by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.addToGroup`. To dismantle ("ungroup") an item group, you can either call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.destroyItemGroup`, or you can manually remove all items from the group by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.removeFromGroup`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 252-256

The operation of adding and removing items preserves the items' scene-relative position and transformation, as opposed to calling setParentItem(), where only the child item's parent-relative position and transformation are kept.

The addtoGroup() function reparents the target item to this item group, keeping the item's position and transformation intact relative to the scene. Visually, this means that items added via :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.addToGroup` will remain completely unchanged as a result of this operation, regardless of the item or the group's current position or transformation; although the item's position and matrix are likely to change.

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.removeFromGroup` function has similar semantics to setParentItem(); it reparents the item to the parent item of the item group. As with :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.addToGroup`, the item's scene-relative position and transformation remain intact.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
