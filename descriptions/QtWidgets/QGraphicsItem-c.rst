.. sip:class-description::
    :status: todo
    :brief: The base class for all graphical items in a QGraphicsScene
    :digest: c8c47945b7fbef1bc80f9a4cda321edc

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` class is the base class for all graphical items in a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

It provides a light-weight foundation for writing your own custom items. This includes defining the item's geometry, collision detection, its painting implementation and item interaction through its event handlers. :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` is part of the `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_

.. image:: ../../../images/graphicsview-items.png

For convenience, Qt provides a set of standard graphics items for the most common shapes. These are:

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem` provides an ellipse item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem` provides a line item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem` provides an arbitrary path item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem` provides a pixmap item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem` provides a polygon item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem` provides a rectangular item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem` provides a simple text label item

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem` provides an advanced text browser item

All of an item's geometric information is based on its local coordinate system. The item's position, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.pos`, is the only function that does not operate in local coordinates, as it returns a position in parent coordinates. `The Graphics View Coordinate System <https://doc.qt.io/qt-6/graphicsview.html#the-graphics-view-coordinate-system>`_ describes the coordinate system in detail.

You can set whether an item should be visible (i.e., drawn, and accepting events), by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setVisible`. Hiding an item will also hide its children. Similarly, you can enable or disable an item by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setEnabled`. If you disable an item, all its children will also be disabled. By default, items are both visible and enabled. To toggle whether an item is selected or not, first enable selection by setting the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsSelectable` flag, and then call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setSelected`. Normally, selection is toggled by the scene, as a result of user interaction.

To write your own graphics item, you first create a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, and then start by implementing its two pure virtual public functions: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`, which returns an estimate of the area painted by the item, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint`, which implements the actual painting. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 54-69

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` function has many different purposes. :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` bases its item index on :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` uses it both for culling invisible items, and for determining the area that needs to be recomposed when drawing overlapping items. In addition, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`'s collision detection mechanisms use :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` to provide an efficient cut-off. The fine grained collision algorithm in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithItem` is based on calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`, which returns an accurate outline of the item's shape as a :sip:ref:`~PyQt6.QtGui.QPainterPath`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` expects all items :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape` to remain unchanged unless it is notified. If you want to change an item's geometry in any way, you must first call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.prepareGeometryChange` to allow :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` to update its bookkeeping.

Collision detection can be done in two ways:

#. Reimplement :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape` to return an accurate shape for your item, and rely on the default implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithItem` to do shape-shape intersection. This can be rather expensive if the shapes are complex.

#. Reimplement :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.collidesWithItem` to provide your own custom item and shape collision algorithm.

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contains` function can be called to determine whether the item *contains* a point or not. This function can also be reimplemented by the item. The default behavior of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contains` is based on calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`.

Items can contain other items, and also be contained by other items. All items can have a parent item and a list of children. Unless the item has no parent, its position is in *parent* coordinates (i.e., the parent's local coordinates). Parent items propagate both their position and their transformation to all children.

.. image:: ../../../images/graphicsview-parentchild.png

.. _qgraphicsitem-transformations:

Transformations
---------------

:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` supports projective transformations in addition to its base position, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.pos`. There are several ways to change an item's transformation. For simple transformations, you can call either of the convenience functions :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale`, or you can pass any transformation matrix to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform`. For advanced transformation control you also have the option of setting several combined transformations by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformations`.

Item transformations accumulate from parent to child, so if both a parent and child item are rotated 90 degrees, the child's total transformation will be 180 degrees. Similarly, if the item's parent is scaled to 2x its original size, its children will also be twice as large. An item's transformation does not affect its own local geometry; all geometry functions (e.g., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contains`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.update`, and all the mapping functions) still operate in local coordinates. For convenience, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` provides the functions :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneTransform`, which returns the item's total transformation matrix (including its position and all parents' positions and transformations), and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scenePos`, which returns its position in scene coordinates. To reset an item's matrix, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.resetTransform`.

Certain transformation operations produce a different outcome depending on the order in which they are applied. For example, if you scale an transform, and then rotate it, you may get a different result than if the transform was rotated first. However, the order you set the transformation properties on :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` does not affect the resulting transformation; :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` always applies the properties in a fixed, defined order:

* The item's base transform is applied (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`)

* The item's transformations list is applied in order (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformations`)

* The item is rotated relative to its transform origin point (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformOriginPoint`)

* The item is scaled relative to its transform origin point (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformOriginPoint`)

.. _qgraphicsitem-painting:

Painting
--------

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint` function is called by :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` to paint the item's contents. The item has no background or default fill of its own; whatever is behind the item will shine through all areas that are not explicitly painted in this function. You can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.update` to schedule a repaint, optionally passing the rectangle that needs a repaint. Depending on whether or not the item is visible in a view, the item may or may not be repainted; there is no equivalent to :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`.

Items are painted by the view, starting with the parent items and then drawing children, in ascending stacking order. You can set an item's stacking order by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setZValue`, and test it by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.zValue`, where items with low z-values are painted before items with high z-values. Stacking order applies to sibling items; parents are always drawn before their children.

.. _qgraphicsitem-sorting:

Sorting
-------

All items are drawn in a defined, stable order, and this same order decides which items will receive mouse input first when you click on the scene. Normally you don't have to worry about sorting, as the items follow a "natural order", following the logical structure of the scene.

An item's children are stacked on top of the parent, and sibling items are stacked by insertion order (i.e., in the same order that they were either added to the scene, or added to the same parent). If you add item A, and then B, then B will be on top of A. If you then add C, the items' stacking order will be A, then B, then C.

.. image:: ../../../images/graphicsview-zorder.png

This example shows the stacking order of all limbs of the robot from the `Drag and Drop Robot <https://doc.qt.io/qt-6/qtwidgets-graphicsview-dragdroprobot-example.html>`_ example. The torso is the root item (all other items are children or descendants of the torso), so it is drawn first. Next, the head is drawn, as it is the first item in the torso's list of children. Then the upper left arm is drawn. As the lower arm is a child of the upper arm, the lower arm is then drawn, followed by the upper arm's next sibling, which is the upper right arm, and so on.

For advanced users, there are ways to alter how your items are sorted:

* You can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setZValue` on an item to explicitly stack it on top of, or under, other sibling items. The default Z value for an item is 0. Items with the same Z value are stacked by insertion order.

* You can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.stackBefore` to reorder the list of children. This will directly modify the insertion order.

* You can set the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemStacksBehindParent` flag to stack a child item behind its parent.

The stacking order of two sibling items also counts for each item's children and descendant items. So if one item is on top of another, then all its children will also be on top of all the other item's children as well.

.. _qgraphicsitem-events:

Events
------

:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` receives events from :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` through the virtual function :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`. This function distributes the most common events to a set of convenience event handlers:

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.contextMenuEvent` handles context menu events

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusInEvent` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusOutEvent` handle focus in and out events

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverMoveEvent`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverLeaveEvent` handles hover enter, move and leave events

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.inputMethodEvent` handles input events, for accessibility support

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.keyPressEvent` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.keyReleaseEvent` handle key press and release events

* :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseReleaseEvent`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseDoubleClickEvent` handles mouse press, move, release, click and doubleclick events

You can filter events for any other item by installing event filters. This functionality is separate from Qt's regular event filters (see :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter`), which only work on subclasses of :sip:ref:`~PyQt6.QtCore.QObject`. After installing your item as an event filter for another item by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.installSceneEventFilter`, the filtered events will be received by the virtual function :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEventFilter`. You can remove item event filters by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.removeSceneEventFilter`.

.. _qgraphicsitem-custom-data:

Custom Data
-----------

Sometimes it's useful to register custom data with an item, be it a custom item, or a standard item. You can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setData` on any item to store data in it using a key-value pair (the key being an integer, and the value is a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_). To get custom data from an item, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.data`. This functionality is completely untouched by Qt itself; it is provided for the user's convenience.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
