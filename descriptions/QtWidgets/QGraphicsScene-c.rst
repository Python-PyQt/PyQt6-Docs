.. sip:class-description::
    :status: todo
    :brief: Surface for managing a large number of 2D graphical items
    :digest: 85bf88ae2aa305de30f9987e7d1d541b

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` class provides a surface for managing a large number of 2D graphical items.

The class serves as a container for QGraphicsItems. It is used together with :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` for visualizing graphical items, such as lines, rectangles, text, or even custom items, on a 2D surface. :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` is part of the `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` also provides functionality that lets you efficiently determine both the location of items, and for determining what items are visible within an arbitrary area on the scene. With the :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` widget, you can either visualize the whole scene, or zoom in and view only parts of the scene.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsscene.py
    :lines: 54-58

Note that :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` has no visual appearance of its own; it only manages the items. You need to create a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` widget to visualize the scene.

To add items to a scene, you start off by constructing a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` object. Then, you have two options: either add your existing :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` objects by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, or you can call one of the convenience functions :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPath`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPolygon`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, or :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, which all return a pointer to the newly added item. The dimensions of the items added with these functions are relative to the item's coordinate system, and the items position is initialized to (0, 0) in the scene.

You can then visualize the scene using :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`. When the scene changes, (e.g., when an item moves or is transformed) :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` emits the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` signal. To remove an item, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.removeItem`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` uses an indexing algorithm to manage the location of items efficiently. By default, a BSP (Binary Space Partitioning) tree is used; an algorithm suitable for large scenes where most items remain static (i.e., do not move around). You can choose to disable this index by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setItemIndexMethod`. For more information about the available indexing algorithms, see the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemIndexMethod` property.

The scene's bounding rect is set by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setSceneRect`. Items can be placed at any position on the scene, and the size of the scene is by default unlimited. The scene rect is used only for internal bookkeeping, maintaining the scene's item index. If the scene rect is unset, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will use the bounding area of all items, as returned by :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemsBoundingRect`, as the scene rect. However, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemsBoundingRect` is a relatively time consuming function, as it operates by collecting positional information for every item on the scene. Because of this, you should always set the scene rect when operating on large scenes.

One of :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`'s greatest strengths is its ability to efficiently determine the location of items. Even with millions of items on the scene, the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` functions can determine the location of an item within a few milliseconds. There are several overloads to :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items`: one that finds items at a certain position, one that finds items inside or intersecting with a polygon or a rectangle, and more. The list of returned items is sorted by stacking order, with the topmost item being the first item in the list. For convenience, there is also an :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemAt` function that returns the topmost item at a given position.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` maintains selection information for the scene. To select items, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setSelectionArea`, and to clear the current selection, call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.clearSelection`. Call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.selectedItems` to get the list of all selected items.

.. _qgraphicsscene-event-handling-and-propagation:

Event Handling and Propagation
------------------------------

Another responsibility that :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` has, is to propagate events from :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`. To send an event to a scene, you construct an event that inherits :sip:ref:`~PyQt6.QtCore.QEvent`, and then send it using, for example, :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendEvent`. :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.event` is responsible for dispatching the event to the individual items. Some common events are handled by convenience event handlers. For example, key press events are handled by :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.keyPressEvent`, and mouse press events are handled by :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.mousePressEvent`.

Key events are delivered to the *focus item*. To set the focus item, you can either call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocusItem`, passing an item that accepts focus, or the item itself can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFocus`. Call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.focusItem` to get the current focus item. For compatibility with widgets, the scene also maintains its own focus information. By default, the scene does not have focus, and all key events are discarded. If :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocus` is called, or if an item on the scene gains focus, the scene automatically gains focus. If the scene has focus, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.hasFocus` will return true, and key events will be forwarded to the focus item, if any. If the scene loses focus, (i.e., someone calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.clearFocus`) while an item has focus, the scene will maintain its item focus information, and once the scene regains focus, it will make sure the last focus item regains focus.

For mouse-over effects, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` dispatches *hover events*. If an item accepts hover events (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptHoverEvents`), it will receive a :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneHoverEnter` event when the mouse enters its area. As the mouse continues moving inside the item's area, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will send it :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneHoverMove` events. When the mouse leaves the item's area, the item will receive a :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneHoverLeave` event.

All mouse events are delivered to the current *mouse grabber* item. An item becomes the scene's mouse grabber if it accepts mouse events (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptedMouseButtons`) and it receives a mouse press. It stays the mouse grabber until it receives a mouse release when no other mouse buttons are pressed. You can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.mouseGrabberItem` to determine what item is currently grabbing the mouse.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`.
