.. sip:class-description::
    :status: todo
    :brief: Base class for all graphics items that require signals, slots and properties
    :digest: 38ce86d4466ec822deb01aa515074155

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject` class provides a base class for all graphics items that require signals, slots and properties.

The class extends a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` with :sip:ref:`~PyQt6.QtCore.QObject`'s signal/slot and property mechanisms. It maps many of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`'s basic setters and getters to properties and adds notification signals for many of them.

.. _qgraphicsobject-parents-and-children:

Parents and Children
--------------------

Each graphics object can be constructed with a parent item. This ensures that the item will be destroyed when its parent item is destroyed. Although :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject` inherits from both :sip:ref:`~PyQt6.QtCore.QObject` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, you should use the functions provided by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, *not* :sip:ref:`~PyQt6.QtCore.QObject`, to manage the relationships between parent and child items.

The relationships between items can be explored using the parentItem() and childItems() functions. In the hierarchy of items in a scene, the parentObject() and parentWidget() functions are the equivalent of the QWidget::parent() and :sip:ref:`~PyQt6.QtWidgets.QWidget.parentWidget` functions for `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ subclasses.

.. seealso:: `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_.
