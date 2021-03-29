.. sip:class-description::
    :status: todo
    :brief: The base class for all layouts in Graphics View
    :digest: 8c6b7d67b6ea055b0b5956cd2d03b1c7

The `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ class provides the base class for all layouts in Graphics View.

`QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ is an abstract class that defines a virtual API for arranging `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ children and other :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` objects for a `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_. `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ assigns responsibility to a `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ through :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setLayout`. As the widget is resized, the layout will automatically arrange the widget's children. `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ inherits :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem`, so, it can be managed by any layout, including its own subclasses.

.. _qgraphicslayout-writing-a-custom-layout:

Writing a Custom Layout
-----------------------

You can use `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ as a base to write your own custom layout (e.g., a flowlayout), but it is more common to use one of its subclasses instead - :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout`. When creating a custom layout, the following functions must be reimplemented as a bare minimum:

+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Function                                                    | Description                                                                                                                                      |
+=============================================================+==================================================================================================================================================+
| :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setGeometry` | Notifies you when the geometry of the layout is set. You can store the geometry in your own layout class in a reimplementation of this function. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint`    | Returns the layout's size hints.                                                                                                                 |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.count`           | Returns the number of items in your layout.                                                                                                      |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.itemAt`          | Returns a pointer to an item in your layout.                                                                                                     |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.removeAt`        | Removes an item from your layout without destroying it.                                                                                          |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

For more details on how to implement each function, refer to the individual function documentation.

Each layout defines its own API for arranging widgets and layout items. For example, with a grid layout, you require a row and a column index with optional row and column spans, alignment, spacing, and more. A linear layout, however, requires a single row or column index to position its items. For a grid layout, the order of insertion does not affect the layout in any way, but for a linear layout, the order is essential. When writing your own layout subclass, you are free to choose the API that best suits your layout.

`QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ provides the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.addChildLayoutItem` convenience function to add layout items to a custom layout. The function will automatically reparent graphics items, if required.

.. _qgraphicslayout-activating-the-layout:

Activating the Layout
---------------------

When the layout's geometry changes, `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ immediately rearranges all of its managed items by calling setGeometry() on each item. This rearrangement is called *activating* the layout.

`QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ updates its own geometry to match the contentsRect() of the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` it is managing. Thus, it will automatically rearrange all its items when the widget is resized. `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ caches the sizes of all its managed items to avoid calling setGeometry() too often.

**Note:** A `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ will have the same geometry as the contentsRect() of the widget (not the layout) it is assigned to.

.. _qgraphicslayout-activating-the-layout-implicitly:

Activating the Layout Implicitly
................................

The layout can be activated implicitly using one of two ways: by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.activate` or by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.invalidate`. Calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.activate` activates the layout immediately. In contrast, calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.invalidate` is delayed, as it posts a :sip:ref:`~PyQt6.QtCore.QEvent.Type.LayoutRequest` event to the managed widget. Due to event compression, the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.activate` will only be called once after control has returned to the event loop. This is referred to as *invalidating* the layout. Invalidating the layout also invalidates any cached information. Also, the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.invalidate` function is a virtual function. So, you can invalidate your own cache in a subclass of `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ by reimplementing this function.

.. _qgraphicslayout-event-handling:

Event Handling
--------------

`QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ listens to events for the widget it manages through the virtual :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.widgetEvent` event handler. When the layout is assigned to a widget, all events delivered to the widget are first processed by :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.widgetEvent`. This allows the layout to be aware of any relevant state changes on the widget such as visibility changes or layout direction changes.

.. _qgraphicslayout-margin-handling:

Margin Handling
---------------

The margins of a `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ can be modified by reimplementing :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.setContentsMargins` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.getContentsMargins`.
