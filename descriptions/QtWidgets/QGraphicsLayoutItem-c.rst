.. sip:class-description::
    :status: todo
    :brief: Can be inherited to allow your custom items to be managed by layouts
    :digest: 7ab106ea218688843e8a0e7aa44643fc

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` class can be inherited to allow your custom items to be managed by layouts.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` is an abstract class that defines a set of virtual functions describing sizes, size policies, and size hints for any object arranged by `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_. The API contains functions relevant for both the item itself and for the user of the item as most of :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem`'s functions are also part of the subclass' public API.

In most cases, existing layout-aware classes such as `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ and `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ already provide the functionality you require. However, subclassing these classes will enable you to create both graphical elements that work well with layouts (`QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_) or custom layouts (`QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_).

.. _qgraphicslayoutitem-subclassing-qgraphicslayoutitem:

Subclassing QGraphicsLayoutItem
-------------------------------

If you create a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` and reimplement its virtual functions, you will enable the layout to resize and position your item along with other QGraphicsLayoutItems including `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ and `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_.

You can start by reimplementing important functions: the protected :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint` function, as well as the public :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setGeometry` function. If you want your items to be aware of immediate geometry changes, you can also reimplement :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.updateGeometry`.

The geometry, size hint, and size policy affect the item's size and position. Calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setGeometry` will always resize and reposition the item immediately. Normally, this function is called by `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ after the layout has been activated, but it can also be called by the item's user at any time.

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint` function returns the item' minimum, preferred and maximum size hints. You can override these properties by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMinimumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setPreferredSize` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMaximumSize`. You can also use functions such as :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMinimumWidth` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMaximumHeight` to set only the width or height component if desired.

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.effectiveSizeHint` function, on the other hand, returns a size hint for any given :sip:ref:`~PyQt6.QtCore.Qt.SizeHint`, and guarantees that the returned size is bound to the minimum and maximum sizes and size hints. You can set the item's vertical and horizontal size policy by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setSizePolicy`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizePolicy` property is used by the layout system to describe how this item prefers to grow or shrink.

.. _qgraphicslayoutitem-nesting-qgraphicslayoutitems:

Nesting QGraphicsLayoutItems
----------------------------

QGraphicsLayoutItems can be nested within other QGraphicsLayoutItems, similar to layouts that can contain sublayouts. This is done either by passing a :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` pointer to :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem`'s protected constructor, or by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setParentLayoutItem`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.parentLayoutItem` function returns a pointer to the item's layoutItem parent. If the item's parent is ``nullptr`` or if the parent does not inherit from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.parentLayoutItem` function then returns ``nullptr``. :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.isLayout` returns ``true`` if the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` subclass is itself a layout, or false otherwise.

Qt uses :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` to provide layout functionality in the `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_, but in the future its use may spread throughout Qt itself.

.. seealso:: `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_, `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout`.
