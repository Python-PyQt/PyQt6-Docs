.. sip:class-description::
    :status: todo
    :brief: Abstract model that can be subclassed to create table models
    :digest: 6de94bfc37b63b4d1258752e2843a7dc

The :sip:ref:`~PyQt6.QtCore.QAbstractTableModel` class provides an abstract model that can be subclassed to create table models.

:sip:ref:`~PyQt6.QtCore.QAbstractTableModel` provides a standard interface for models that represent their data as a two-dimensional array of items. It is not used directly, but must be subclassed.

Since the model provides a more specialized interface than :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, it is not suitable for use with tree views, although it can be used to provide data to a :sip:ref:`~PyQt6.QtWidgets.QListView`. If you need to represent a simple list of items, and only need a model to contain a single column of data, subclassing the :sip:ref:`~PyQt6.QtCore.QAbstractListModel` may be more appropriate.

The rowCount() and columnCount() functions return the dimensions of the table. To retrieve a model index corresponding to an item in the model, use :sip:ref:`~PyQt6.QtCore.QAbstractTableModel.index` and provide only the row and column numbers.

.. _qabstracttablemodel-subclassing:

Subclassing
-----------

When subclassing :sip:ref:`~PyQt6.QtCore.QAbstractTableModel`, you must implement rowCount(), columnCount(), and data(). Default implementations of the :sip:ref:`~PyQt6.QtCore.QAbstractTableModel.index` and :sip:ref:`~PyQt6.QtCore.QAbstractTableModel.parent` functions are provided by :sip:ref:`~PyQt6.QtCore.QAbstractTableModel`. Well behaved models will also implement headerData().

Editable models need to implement setData(), and implement :sip:ref:`~PyQt6.QtCore.QAbstractTableModel.flags` to return a value containing Qt::ItemIsEditable.

Models that provide interfaces to resizable data structures can provide implementations of insertRows(), removeRows(), insertColumns(), and removeColumns(). When implementing these functions, it is important to call the appropriate functions so that all connected views are aware of any changes:

* An insertRows() implementation must call beginInsertRows() *before* inserting new rows into the data structure, and it must call endInsertRows() *immediately afterwards*.

* An insertColumns() implementation must call beginInsertColumns() *before* inserting new columns into the data structure, and it must call endInsertColumns() *immediately afterwards*.

* A removeRows() implementation must call beginRemoveRows() *before* the rows are removed from the data structure, and it must call endRemoveRows() *immediately afterwards*.

* A removeColumns() implementation must call beginRemoveColumns() *before* the columns are removed from the data structure, and it must call endRemoveColumns() *immediately afterwards*.

**Note:** Some general guidelines for subclassing models are available in the `Model Subclassing Reference <https://doc.qt.io/qt-6/model-view-programming.html#model-subclassing-reference>`_.

.. _qabstracttablemodel-thread-safety:

Thread safety
-------------

Being a subclass of QObject, :sip:ref:`~PyQt6.QtCore.QAbstractTableModel` is not thread-safe. Any :sip:ref:`~PyQt6.QtCore.QAbstractTableModel` model-related API should only be called from the thread the model object lives in. If the :sip:ref:`~PyQt6.QtCore.QAbstractTableModel` is connected with a view, that means the GUI thread, as that is where the view lives, and it will call into the model from the GUI thread. Using a background thread to populate or modify the contents of a model is possible, but requires care, as the background thread cannot call any model-related API directly. Instead, you should queue the updates and apply them in the main thread. This can be done with queued connections.

.. seealso:: `Model Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-classes>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, :sip:ref:`~PyQt6.QtCore.QAbstractListModel`.
