.. sip:class-description::
    :status: todo
    :brief: Generic model for storing custom data
    :digest: 372009849ee5dbbca937afa8a1dc3172

The :sip:ref:`~PyQt6.QtGui.QStandardItemModel` class provides a generic model for storing custom data.

:sip:ref:`~PyQt6.QtGui.QStandardItemModel` can be used as a repository for standard Qt data types. It is one of the Model/View Classes and is part of Qt's model/view framework.

:sip:ref:`~PyQt6.QtGui.QStandardItemModel` provides a classic item-based approach to working with the model. The items in a :sip:ref:`~PyQt6.QtGui.QStandardItemModel` are provided by :sip:ref:`~PyQt6.QtGui.QStandardItem`.

:sip:ref:`~PyQt6.QtGui.QStandardItemModel` implements the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` interface, which means that the model can be used to provide data in any view that supports that interface (such as QListView, QTableView and QTreeView, and your own custom views). For performance and flexibility, you may want to subclass :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` to provide support for different kinds of data repositories. For example, the :sip:ref:`~PyQt6.QtGui.QFileSystemModel` provides a model interface to the underlying file system.

When you want a list or tree, you typically create an empty :sip:ref:`~PyQt6.QtGui.QStandardItemModel` and use :sip:ref:`~PyQt6.QtGui.QStandardItemModel.appendRow` to add items to the model, and :sip:ref:`~PyQt6.QtGui.QStandardItemModel.item` to access an item. If your model represents a table, you typically pass the dimensions of the table to the :sip:ref:`~PyQt6.QtGui.QStandardItemModel` constructor and use :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setItem` to position items into the table. You can also use :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setRowCount` and :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setColumnCount` to alter the dimensions of the model. To insert items, use :sip:ref:`~PyQt6.QtGui.QStandardItemModel.insertRow` or :sip:ref:`~PyQt6.QtGui.QStandardItemModel.insertColumn`, and to remove items, use removeRow() or removeColumn().

You can set the header labels of your model with :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setHorizontalHeaderLabels` and :sip:ref:`~PyQt6.QtGui.QStandardItemModel.setVerticalHeaderLabels`.

You can search for items in the model with :sip:ref:`~PyQt6.QtGui.QStandardItemModel.findItems`, and sort the model by calling :sip:ref:`~PyQt6.QtGui.QStandardItemModel.sort`.

Call :sip:ref:`~PyQt6.QtGui.QStandardItemModel.clear` to remove all items from the model.

An example usage of :sip:ref:`~PyQt6.QtGui.QStandardItemModel` to create a table:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_itemviews_qstandarditemmodel.py
    :lines: 68-74

An example usage of :sip:ref:`~PyQt6.QtGui.QStandardItemModel` to create a tree:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_itemviews_qstandarditemmodel.py
    :lines: 83-89

After setting the model on a view, you typically want to react to user actions, such as an item being clicked. Since a QAbstractItemView provides :sip:ref:`~PyQt6.QtCore.QModelIndex`-based signals and functions, you need a way to obtain the :sip:ref:`~PyQt6.QtGui.QStandardItem` that corresponds to a given :sip:ref:`~PyQt6.QtCore.QModelIndex`, and vice versa. :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemFromIndex` and :sip:ref:`~PyQt6.QtGui.QStandardItemModel.indexFromItem` provide this mapping. Typical usage of :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemFromIndex` includes obtaining the item at the current index in a view, and obtaining the item that corresponds to an index carried by a QAbstractItemView signal, such as QAbstractItemView::clicked(). First you connect the view's signal to a slot in your class:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_itemviews_qstandarditemmodel.py
    :lines: 97-100

When you receive the signal, you call :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemFromIndex` on the given model index to get a pointer to the item:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_itemviews_qstandarditemmodel.py
    :lines: 107-111

Conversely, you must obtain the :sip:ref:`~PyQt6.QtCore.QModelIndex` of an item when you want to invoke a model/view function that takes an index as argument. You can obtain the index either by using the model's :sip:ref:`~PyQt6.QtGui.QStandardItemModel.indexFromItem` function, or, equivalently, by calling :sip:ref:`~PyQt6.QtGui.QStandardItem.index`:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_itemviews_qstandarditemmodel.py
    :lines: 119-119

You are, of course, not required to use the item-based approach; you could instead rely entirely on the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` interface when working with the model, or use a combination of the two as appropriate.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`.
