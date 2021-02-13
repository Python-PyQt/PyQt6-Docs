.. sip:class-description::
    :status: todo
    :brief: Default model/view implementation of a tree view
    :digest: 7686d685dd6ab10bedf7a62d904c2253

The :sip:ref:`~PyQt6.QtWidgets.QTreeView` class provides a default model/view implementation of a tree view.

.. image:: ../../../images/windows-treeview.png

A :sip:ref:`~PyQt6.QtWidgets.QTreeView` implements a tree representation of items from a model. This class is used to provide standard hierarchical lists that were previously provided by the ``QListView`` class, but using the more flexible approach provided by Qt's model/view architecture.

The :sip:ref:`~PyQt6.QtWidgets.QTreeView` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

:sip:ref:`~PyQt6.QtWidgets.QTreeView` implements the interfaces defined by the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` class to allow it to display data provided by models derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class.

It is simple to construct a tree view displaying data from a model. In the following example, the contents of a directory are supplied by a :sip:ref:`~PyQt6.QtGui.QFileSystemModel` and displayed as a tree:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-shareddirmodel-main.py
    :lines: 69-72

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-shareddirmodel-main.py
    :lines: 74-74

The model/view architecture ensures that the contents of the tree view are updated as the model changes.

Items that have children can be in an expanded (children are visible) or collapsed (children are hidden) state. When this state changes a :sip:ref:`~PyQt6.QtWidgets.QTreeView.collapsed` or :sip:ref:`~PyQt6.QtWidgets.QTreeView.expanded` signal is emitted with the model index of the relevant item.

The amount of indentation used to indicate levels of hierarchy is controlled by the :sip:ref:`~PyQt6.QtWidgets.QTreeView.indentation` property.

Headers in tree views are constructed using the :sip:ref:`~PyQt6.QtWidgets.QHeaderView` class and can be hidden using ``header()->hide()``. Note that each header is configured with its :sip:ref:`~PyQt6.QtWidgets.QHeaderView.stretchLastSection` property set to true, ensuring that the view does not waste any of the space assigned to it for its header. If this value is set to true, this property will override the resize mode set on the last section in the header.

By default, all columns in a tree view are movable except the first. To disable movement of these columns, use :sip:ref:`~PyQt6.QtWidgets.QHeaderView`'s :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setSectionsMovable` function. For more information about rearranging sections, see Moving Header Sections.

.. _qtreeview-key-bindings:

Key Bindings
------------

:sip:ref:`~PyQt6.QtWidgets.QTreeView` supports a set of key bindings that enable the user to navigate in the view and interact with the contents of items:

+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key      | Action                                                                                                                                                                                                                                 |
+==========+========================================================================================================================================================================================================================================+
| Up       | Moves the cursor to the item in the same column on the previous row. If the parent of the current item has no more rows to navigate to, the cursor moves to the relevant item in the last row of the sibling that precedes the parent. |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Down     | Moves the cursor to the item in the same column on the next row. If the parent of the current item has no more rows to navigate to, the cursor moves to the relevant item in the first row of the sibling that follows the parent.     |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Left     | Hides the children of the current item (if present) by collapsing a branch.                                                                                                                                                            |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Minus    | Same as Left.                                                                                                                                                                                                                          |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Right    | Reveals the children of the current item (if present) by expanding a branch.                                                                                                                                                           |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Plus     | Same as Right.                                                                                                                                                                                                                         |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Asterisk | Expands the current item and all its children (if present).                                                                                                                                                                            |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PageUp   | Moves the cursor up one page.                                                                                                                                                                                                          |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PageDown | Moves the cursor down one page.                                                                                                                                                                                                        |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Home     | Moves the cursor to an item in the same column of the first row of the first top-level item in the model.                                                                                                                              |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| End      | Moves the cursor to an item in the same column of the last row of the last top-level item in the model.                                                                                                                                |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F2       | In editable models, this opens the current item for editing. The Escape key can be used to cancel the editing process and revert any changes to the data displayed.                                                                    |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _qtreeview-improving-performance:

Improving Performance
---------------------

It is possible to give the view hints about the data it is handling in order to improve its performance when displaying large numbers of items. One approach that can be taken for views that are intended to display items with equal heights is to set the :sip:ref:`~PyQt6.QtWidgets.QTreeView.uniformRowHeights` property to true.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListView`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidget`, `View Classes <https://doc.qt.io/qt-6/model-view-programming.html#view-classes>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, `Dir View Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-dirview-example.html>`_.
