.. sip:class-description::
    :status: todo
    :brief: Grid layout for managing widgets in Graphics View
    :digest: ea08e3b2f1d25db4ca15e8fcd5b82ad1

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout` class provides a grid layout for managing widgets in Graphics View.

The most common way to use :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout` is to construct an object on the heap, passing a parent widget to the constructor, then add widgets and layouts by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.addItem`. :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout` automatically computes the dimensions of the grid as you add items.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsgridlayout.py
    :lines: 54-64

Alternatively, if you do not pass a parent widget to the layout's constructor, you will need to call :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setLayout` to set this layout as the top-level layout for that widget, the widget will take ownership of the layout.

The layout takes ownership of the items. In some cases when the layout item also inherits from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` (such as :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget`) there will be a ambiguity in ownership because the layout item belongs to two ownership hierarchies. See the documentation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setOwnedByLayout` how to handle this. You can access each item in the layout by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.count` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.itemAt`. Calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.removeAt` will remove an item from the layout, without destroying it.

.. _qgraphicsgridlayout-size-hints-and-size-policies-in-qgraphicsgridlayout:

Size Hints and Size Policies in QGraphicsGridLayout
---------------------------------------------------

:sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout` respects each item's size hints and size policies, and when a cell in the grid has more space than the items can fill, each item is arranged according to the layout's alignment for that item. You can set an alignment for each item by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.setAlignment`, and check the alignment for any item by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.alignment`. You can also set the alignment for an entire row or column by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.setRowAlignment` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout.setColumnAlignment` respectively. By default, items are aligned to the top left.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget`.
