.. sip:class-description::
    :status: todo
    :brief: Abstract model that can be subclassed to create one-dimensional list models
    :digest: 5929c6671bb26f062bd236fe54574d92

The :sip:ref:`~PyQt6.QtCore.QAbstractListModel` class provides an abstract model that can be subclassed to create one-dimensional list models.

:sip:ref:`~PyQt6.QtCore.QAbstractListModel` provides a standard interface for models that represent their data as a simple non-hierarchical sequence of items. It is not used directly, but must be subclassed.

Since the model provides a more specialized interface than :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, it is not suitable for use with tree views; you will need to subclass :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` if you want to provide a model for that purpose. If you need to use a number of list models to manage data, it may be more appropriate to subclass :sip:ref:`~PyQt6.QtCore.QAbstractTableModel` instead.

Simple models can be created by subclassing this class and implementing the minimum number of required functions. For example, we could implement a simple read-only QStringList-based model that provides a list of strings to a :sip:ref:`~PyQt6.QtWidgets.QListView` widget. In such a case, we only need to implement the rowCount() function to return the number of items in the list, and the data() function to retrieve items from the list.

Since the model represents a one-dimensional structure, the rowCount() function returns the total number of items in the model. The columnCount() function is implemented for interoperability with all kinds of views, but by default informs views that the model contains only one column.

.. _qabstractlistmodel-subclassing:

Subclassing
-----------

When subclassing :sip:ref:`~PyQt6.QtCore.QAbstractListModel`, you must provide implementations of the rowCount() and data() functions. Well behaved models also provide a headerData() implementation.

If your model is used within QML and requires roles other than the default ones provided by the roleNames() function, you must override it.

For editable list models, you must also provide an implementation of setData(), and implement the :sip:ref:`~PyQt6.QtCore.QAbstractListModel.flags` function so that it returns a value containing Qt::ItemIsEditable.

Note that :sip:ref:`~PyQt6.QtCore.QAbstractListModel` provides a default implementation of columnCount() that informs views that there is only a single column of items in this model.

Models that provide interfaces to resizable list-like data structures can provide implementations of insertRows() and removeRows(). When implementing these functions, it is important to call the appropriate functions so that all connected views are aware of any changes:

* An insertRows() implementation must call beginInsertRows() *before* inserting new rows into the data structure, and it must call endInsertRows() *immediately afterwards*.

* A removeRows() implementation must call beginRemoveRows() *before* the rows are removed from the data structure, and it must call endRemoveRows() *immediately afterwards*.

**Note:** Some general guidelines for subclassing models are available in the `Model Subclassing Reference <https://doc.qt.io/qt-6/model-view-programming.html#model-subclassing-reference>`_.

.. seealso:: `Model Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-classes>`_, `Model Subclassing Reference <https://doc.qt.io/qt-6/model-view-programming.html#model-subclassing-reference>`_, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, :sip:ref:`~PyQt6.QtCore.QAbstractTableModel`, `Item Views Puzzle Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-puzzle-example.html>`_.
