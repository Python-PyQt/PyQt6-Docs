.. sip:class-description::
    :status: todo
    :brief: Tree view that uses a predefined tree model
    :digest: aea1ffe8bc731158692f1b75c53c8908

The :sip:ref:`~PyQt6.QtWidgets.QTreeWidget` class provides a tree view that uses a predefined tree model.

.. image:: ../../../images/windows-treeview.png

The :sip:ref:`~PyQt6.QtWidgets.QTreeWidget` class is a convenience class that provides a standard tree widget with a classic item-based interface similar to that used by the :sip:ref:`~PyQt6.QtWidgets.QListView` class in Qt 3. This class is based on Qt's Model/View architecture and uses a default model to hold items, each of which is a :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`.

Developers who do not need the flexibility of the Model/View framework can use this class to create simple hierarchical lists very easily. A more flexible approach involves combining a :sip:ref:`~PyQt6.QtWidgets.QTreeView` with a standard item model. This allows the storage of data to be separated from its representation.

In its simplest form, a tree widget can be constructed in the following way:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qtreewidget.py
    :lines: 54-59

Before items can be added to the tree widget, the number of columns must be set with :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.setColumnCount`. This allows each item to have one or more labels or other decorations. The number of columns in use can be found with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.columnCount` function.

The tree can have a header that contains a section for each column in the widget. It is easiest to set up the labels for each section by supplying a list of strings with :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.setHeaderLabels`, but a custom header can be constructed with a :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem` and inserted into the tree with the :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.setHeaderItem` function.

The items in the tree can be sorted by column according to a predefined sort order. If sorting is enabled, the user can sort the items by clicking on a column header. Sorting can be enabled or disabled by calling :sip:ref:`~PyQt6.QtWidgets.QTreeView.setSortingEnabled`. The :sip:ref:`~PyQt6.QtWidgets.QTreeView.isSortingEnabled` function indicates whether sorting is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItemIterator`, :sip:ref:`~PyQt6.QtWidgets.QTreeView`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, `Settings Editor Example <https://doc.qt.io/qt-6/qtwidgets-tools-settingseditor-example.html>`_.
