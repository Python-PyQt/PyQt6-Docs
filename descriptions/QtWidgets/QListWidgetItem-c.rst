.. sip:class-description::
    :status: todo
    :brief: Item for use with the QListWidget item view class
    :digest: f58e117e30f0a30b99a80d331680f37f

The :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem` class provides an item for use with the :sip:ref:`~PyQt6.QtWidgets.QListWidget` item view class.

A :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem` represents a single item in a :sip:ref:`~PyQt6.QtWidgets.QListWidget`. Each item can hold several pieces of information, and will display them appropriately.

The item view convenience classes use a classic item-based interface rather than a pure model/view approach. For a more flexible list view widget, consider using the :sip:ref:`~PyQt6.QtWidgets.QListView` class with a standard model.

List items can be inserted automatically into a list, when they are constructed, by specifying the list widget:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qlistwidget-using-mainwindow.py
    :lines: 106-106

Alternatively, list items can also be created without a parent widget, and later inserted into a list using :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem`.

List items are typically used to display :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.text` and an :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.icon`. These are set with the :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setText` and :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setIcon` functions. The appearance of the text can be customized with :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setFont`, :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setForeground`, and :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setBackground`. Text in list items can be aligned using the :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setTextAlignment` function. Tooltips, status tips and "What's This?" help can be added to list items with :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setToolTip`, :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setStatusTip`, and :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setWhatsThis`.

By default, items are enabled, selectable, checkable, and can be the source of drag and drop operations.

Each item's flags can be changed by calling :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setFlags` with the appropriate value (see Qt::ItemFlags). Checkable items can be checked, unchecked and partially checked with the :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setCheckState` function. The corresponding :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.checkState` function indicates the item's current check state.

The :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.isHidden` function can be used to determine whether the item is hidden. To hide an item, use :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.setHidden`.

.. _qlistwidgetitem-subclassing:

Subclassing
-----------

When subclassing :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem` to provide custom items, it is possible to define new types for them enabling them to be distinguished from standard items. For subclasses that require this feature, ensure that you call the base class constructor with a new type value equal to or greater than :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.ItemType.UserType`, within *your* constructor.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListWidget`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`, :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`.
