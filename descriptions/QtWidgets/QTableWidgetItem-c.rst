.. sip:class-description::
    :status: todo
    :brief: Item for use with the QTableWidget class
    :digest: b4cb616195e4ff9f5294e7560b44e5c9

The :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem` class provides an item for use with the :sip:ref:`~PyQt6.QtWidgets.QTableWidget` class.

Table items are used to hold pieces of information for table widgets. Items usually contain text, icons, or checkboxes

The :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem` class is a convenience class that replaces the ``QTableItem`` class in Qt 3. It provides an item for use with the :sip:ref:`~PyQt6.QtWidgets.QTableWidget` class.

Top-level items are constructed without a parent then inserted at the position specified by a pair of row and column numbers:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtablewidget-using-mainwindow.py
    :lines: 109-111

Each item can have its own background brush which is set with the :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.setBackground` function. The current background brush can be found with :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.background`. The text label for each item can be rendered with its own font and brush. These are specified with the :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.setFont` and :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.setForeground` functions, and read with :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.font` and :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.foreground`.

By default, items are enabled, editable, selectable, checkable, and can be used both as the source of a drag and drop operation and as a drop target. Each item's flags can be changed by calling :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.setFlags` with the appropriate value (see Qt::ItemFlags). Checkable items can be checked and unchecked with the :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.setCheckState` function. The corresponding :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.checkState` function indicates whether the item is currently checked.

.. _qtablewidgetitem-subclassing:

Subclassing
-----------

When subclassing :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem` to provide custom items, it is possible to define new types for them so that they can be distinguished from standard items. The constructors for subclasses that require this feature need to call the base class constructor with a new type value equal to or greater than :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.ItemType.UserType`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`.
