.. sip:class-description::
    :status: todo
    :brief: Item for use with the QStandardItemModel class
    :digest: e34942b179e17ed3be06785b214a5dea

The :sip:ref:`~PyQt6.QtGui.QStandardItem` class provides an item for use with the :sip:ref:`~PyQt6.QtGui.QStandardItemModel` class.

Items usually contain text, icons, or checkboxes.

Each item can have its own background brush which is set with the :sip:ref:`~PyQt6.QtGui.QStandardItem.setBackground` function. The current background brush can be found with :sip:ref:`~PyQt6.QtGui.QStandardItem.background`. The text label for each item can be rendered with its own font and brush. These are specified with the :sip:ref:`~PyQt6.QtGui.QStandardItem.setFont` and :sip:ref:`~PyQt6.QtGui.QStandardItem.setForeground` functions, and read with :sip:ref:`~PyQt6.QtGui.QStandardItem.font` and :sip:ref:`~PyQt6.QtGui.QStandardItem.foreground`.

By default, items are enabled, editable, selectable, checkable, and can be used both as the source of a drag and drop operation and as a drop target. Each item's flags can be changed by calling :sip:ref:`~PyQt6.QtGui.QStandardItem.setFlags`. Checkable items can be checked and unchecked with the :sip:ref:`~PyQt6.QtGui.QStandardItem.setCheckState` function. The corresponding :sip:ref:`~PyQt6.QtGui.QStandardItem.checkState` function indicates whether the item is currently checked.

You can store application-specific data in an item by calling :sip:ref:`~PyQt6.QtGui.QStandardItem.setData`.

Each item can have a two-dimensional table of child items. This makes it possible to build hierarchies of items. The typical hierarchy is the tree, in which case the child table is a table with a single column (a list).

The dimensions of the child table can be set with :sip:ref:`~PyQt6.QtGui.QStandardItem.setRowCount` and :sip:ref:`~PyQt6.QtGui.QStandardItem.setColumnCount`. Items can be positioned in the child table with :sip:ref:`~PyQt6.QtGui.QStandardItem.setChild`. Get a pointer to a child item with :sip:ref:`~PyQt6.QtGui.QStandardItem.child`. New rows and columns of children can also be inserted with :sip:ref:`~PyQt6.QtGui.QStandardItem.insertRow` and :sip:ref:`~PyQt6.QtGui.QStandardItem.insertColumn`, or appended with :sip:ref:`~PyQt6.QtGui.QStandardItem.appendRow` and :sip:ref:`~PyQt6.QtGui.QStandardItem.appendColumn`. When using the append and insert functions, the dimensions of the child table will grow as needed.

An existing row of children can be removed with :sip:ref:`~PyQt6.QtGui.QStandardItem.removeRow` or :sip:ref:`~PyQt6.QtGui.QStandardItem.takeRow`; correspondingly, a column can be removed with :sip:ref:`~PyQt6.QtGui.QStandardItem.removeColumn` or :sip:ref:`~PyQt6.QtGui.QStandardItem.takeColumn`.

An item's children can be sorted by calling :sip:ref:`~PyQt6.QtGui.QStandardItem.sortChildren`.

.. _qstandarditem-subclassing:

Subclassing
-----------

When subclassing :sip:ref:`~PyQt6.QtGui.QStandardItem` to provide custom items, it is possible to define new types for them so that they can be distinguished from the base class. The :sip:ref:`~PyQt6.QtGui.QStandardItem.type` function should be reimplemented to return a new type value equal to or greater than :sip:ref:`~PyQt6.QtGui.QStandardItem.ItemType.UserType`.

Reimplement :sip:ref:`~PyQt6.QtGui.QStandardItem.data` and :sip:ref:`~PyQt6.QtGui.QStandardItem.setData` if you want to perform custom handling of data queries and/or control how an item's data is represented.

Reimplement :sip:ref:`~PyQt6.QtGui.QStandardItem.clone` if you want :sip:ref:`~PyQt6.QtGui.QStandardItemModel` to be able to create instances of your custom item class on demand (see :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setItemPrototype`).

Reimplement :sip:ref:`~PyQt6.QtGui.QStandardItem.read` and :sip:ref:`~PyQt6.QtGui.QStandardItem.write` if you want to control how items are represented in their serialized form.

Reimplement operator<() if you want to control the semantics of item comparison. operator<() determines the sorted order when sorting items with :sip:ref:`~PyQt6.QtGui.QStandardItem.sortChildren` or with :sip:ref:`~PyQt6.QtGui.QStandardItemModel.sort`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel`, `Item View Convenience Classes <https://doc.qt.io/qt-6/model-view-programming.html#item-view-convenience-classes>`_, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.
