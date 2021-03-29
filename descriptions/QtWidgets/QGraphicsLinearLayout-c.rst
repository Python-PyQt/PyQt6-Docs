.. sip:class-description::
    :status: todo
    :brief: Horizontal or vertical layout for managing widgets in Graphics View
    :digest: c140336362d395aa99f31e21c46e6d54

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout` class provides a horizontal or vertical layout for managing widgets in Graphics View.

The default orientation for a linear layout is :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Horizontal`. You can choose a vertical orientation either by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.setOrientation`, or by passing :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Vertical` to :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout`'s constructor.

The most common way to use :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout` is to construct an object on the heap with no parent, add widgets and layouts by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.addItem`, and finally assign the layout to a widget by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setLayout`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicslinearlayout.py
    :lines: 54-64

You can add widgets, layouts, stretches (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.addStretch`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.insertStretch` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.setStretchFactor`), and spacings (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.setItemSpacing`) to a linear layout. The layout takes ownership of the items. In some cases when the layout item also inherits from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` (such as `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_) there will be a ambiguity in ownership because the layout item belongs to two ownership hierarchies. See the documentation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setOwnedByLayout` how to handle this. You can access each item in the layout by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.count` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.itemAt`. Calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.removeAt` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.removeItem` will remove an item from the layout, without destroying it.

.. _qgraphicslinearlayout-size-hints-and-size-policies-in-qgraphicslinearlayout:

Size Hints and Size Policies in QGraphicsLinearLayout
-----------------------------------------------------

:sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout` respects each item's size hints and size policies, and when the layout contains more space than the items can fill, each item is arranged according to the layout's alignment for that item. You can set an alignment for each item by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.setAlignment`, and check the alignment for any item by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.alignment`. By default, items are aligned to the top left.

.. _qgraphicslinearlayout-spacing-within-qgraphicslinearlayout:

Spacing within QGraphicsLinearLayout
------------------------------------

Between the items, the layout distributes some space. The actual amount of space depends on the managed widget's current style, but the common spacing is 4. You can also set your own spacing by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.setSpacing`, and get the current spacing value by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.spacing`. If you want to configure individual spacing for your items, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.setItemSpacing`.

.. _qgraphicslinearlayout-stretch-factor-in-qgraphicslinearlayout:

Stretch Factor in QGraphicsLinearLayout
---------------------------------------

You can assign a stretch factor to each item to control how much space it will get compared to the other items. By default, two identical widgets arranged in a linear layout will have the same size, but if the first widget has a stretch factor of 1 and the second widget has a stretch factor of 2, the first widget will get 1/3 of the available space, and the second will get 2/3.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout` calculates the distribution of sizes by adding up the stretch factors of all items, and then dividing the available space accordingly. The default stretch factor is 0 for all items; a factor of 0 means the item does not have any defined stretch factor; effectively this is the same as setting the stretch factor to 1. The stretch factor only applies to the available space in the lengthwise direction of the layout (following its orientation). If you want to control both the item's horizontal and vertical stretch, you can use :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout` instead.

.. _qgraphicslinearlayout-qgraphicslinearlayout-compared-to-other-layouts:

QGraphicsLinearLayout Compared to Other Layouts
-----------------------------------------------

:sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout` is very similar to :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout` and :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout`, but in contrast to these classes, it is used to manage `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ and `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ instead of `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ and :sip:ref:`~PyQt6.QtWidgets.QLayout`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout`, `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_.
