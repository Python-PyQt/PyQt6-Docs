.. sip:class-description::
    :status: todo
    :brief: Item for use with the QTreeWidget convenience class
    :digest: 4b3d47b2a6a3ece8c32254d7dd848aed

The :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem` class provides an item for use with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidget` convenience class.

Tree widget items are used to hold rows of information for tree widgets. Rows usually contain several columns of data, each of which can contain a text label and an icon.

The :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem` class is a convenience class that replaces the QListViewItem class in Qt 3. It provides an item for use with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidget` class.

Items are usually constructed with a parent that is either a :sip:ref:`~PyQt6.QtWidgets.QTreeWidget` (for top-level items) or a :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem` (for items on lower levels of the tree). For example, the following code constructs a top-level item to represent cities of the world, and adds a entry for Oslo as a child item:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtreewidget-using-mainwindow.py
    :lines: 115-119

Items can be added in a particular order by specifying the item they follow when they are constructed:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtreewidget-using-mainwindow.py
    :lines: 127-129

Each column in an item can have its own background brush which is set with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setBackground` function. The current background brush can be found with :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.background`. The text label for each column can be rendered with its own font and brush. These are specified with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setFont` and :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setForeground` functions, and read with :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.font` and :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.foreground`.

The main difference between top-level items and those in lower levels of the tree is that a top-level item has no :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.parent`. This information can be used to tell the difference between items, and is useful to know when inserting and removing items from the tree. Children of an item can be removed with :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.takeChild` and inserted at a given index in the list of children with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.insertChild` function.

By default, items are enabled, selectable, checkable, and can be the source of a drag and drop operation. Each item's flags can be changed by calling :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setFlags` with the appropriate value (see Qt::ItemFlags). Checkable items can be checked and unchecked with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setCheckState` function. The corresponding :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.checkState` function indicates whether the item is currently checked.

.. _qtreewidgetitem-subclassing:

Subclassing
-----------

When subclassing :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem` to provide custom items, it is possible to define new types for them so that they can be distinguished from standard items. The constructors for subclasses that require this feature need to call the base class constructor with a new type value equal to or greater than :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.ItemType.UserType`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidget`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItemIterator`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`, :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`.
