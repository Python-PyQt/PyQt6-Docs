.. sip:class-description::
    :status: todo
    :brief: Item-based list widget
    :digest: 4c7bd1d9cf19a6ed7b01e547b9db3d8a

The :sip:ref:`~PyQt6.QtWidgets.QListWidget` class provides an item-based list widget.

.. image:: ../../../images/windows-listview.png

:sip:ref:`~PyQt6.QtWidgets.QListWidget` is a convenience class that provides a list view similar to the one supplied by :sip:ref:`~PyQt6.QtWidgets.QListView`, but with a classic item-based interface for adding and removing items. :sip:ref:`~PyQt6.QtWidgets.QListWidget` uses an internal model to manage each :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem` in the list.

For a more flexible list view widget, use the :sip:ref:`~PyQt6.QtWidgets.QListView` class with a standard model.

List widgets are constructed in the same way as other widgets:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qlistwidget-using-mainwindow.py
    :lines: 76-76

The selectionMode() of a list widget determines how many of the items in the list can be selected at the same time, and whether complex selections of items can be created. This can be set with the setSelectionMode() function.

There are two ways to add items to the list: they can be constructed with the list widget as their parent widget, or they can be constructed with no parent widget and added to the list later. If a list widget already exists when the items are constructed, the first method is easier to use:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qlistwidget-using-mainwindow.py
    :lines: 100-102

If you need to insert a new item into the list at a particular position, then it should be constructed without a parent widget. The :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem` function should then be used to place it within the list. The list widget will take ownership of the item.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qlistwidget-using-mainwindow.py
    :lines: 142-143

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qlistwidget-using-mainwindow.py
    :lines: 147-147

For multiple items, :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItems` can be used instead. The number of items in the list is found with the :sip:ref:`~PyQt6.QtWidgets.QListWidget.count` function. To remove items from the list, use :sip:ref:`~PyQt6.QtWidgets.QListWidget.takeItem`.

The current item in the list can be found with :sip:ref:`~PyQt6.QtWidgets.QListWidget.currentItem`, and changed with :sip:ref:`~PyQt6.QtWidgets.QListWidget.setCurrentItem`. The user can also change the current item by navigating with the keyboard or clicking on a different item. When the current item changes, the :sip:ref:`~PyQt6.QtWidgets.QListWidget.currentItemChanged` signal is emitted with the new current item and the item that was previously current.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`, :sip:ref:`~PyQt6.QtWidgets.QListView`, :sip:ref:`~PyQt6.QtWidgets.QTreeView`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, `Tab Dialog Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-tabdialog-example.html>`_.
