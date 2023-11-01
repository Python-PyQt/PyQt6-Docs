.. sip:class-description::
    :status: todo
    :brief: The abstract interface for item model classes
    :digest: 20198ea0f5437ad94d864e4c8629bec0

The :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class provides the abstract interface for item model classes.

The :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class defines the standard interface that item models must use to be able to interoperate with other components in the model/view architecture. It is not supposed to be instantiated directly. Instead, you should subclass it to create new models.

The :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_. It can be used as the underlying data model for the item view elements in QML or the item view classes in the Qt Widgets module.

If you need a model to use with an item view such as QML's List View element or the C++ widgets :sip:ref:`~PyQt6.QtWidgets.QListView` or :sip:ref:`~PyQt6.QtWidgets.QTableView`, you should consider subclassing :sip:ref:`~PyQt6.QtCore.QAbstractListModel` or :sip:ref:`~PyQt6.QtCore.QAbstractTableModel` instead of this class.

The underlying data model is exposed to views and delegates as a hierarchy of tables. If you do not make use of the hierarchy, then the model is a simple table of rows and columns. Each item has a unique index specified by a :sip:ref:`~PyQt6.QtCore.QModelIndex`.

.. image:: ../../../images/modelindex-no-parent.png

Every item of data that can be accessed via a model has an associated model index. You can obtain this model index using the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.index` function. Each index may have a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.sibling` index; child items have a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.parent` index.

Each item has a number of data elements associated with it and they can be retrieved by specifying a role (see :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`) to the model's :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data` function. Data for all available roles can be obtained at the same time using the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.itemData` function.

Data for each role is set using a particular :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`. Data for individual roles are set individually with :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData`, or they can be set for all roles with :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setItemData`.

Items can be queried with :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.flags` (see :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`) to see if they can be selected, dragged, or manipulated in other ways.

If an item has child objects, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.hasChildren` returns ``true`` for the corresponding index.

The model has a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowCount` and a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.columnCount` for each level of the hierarchy. Rows and columns can be inserted and removed with :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows`, and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumns`.

The model emits signals to indicate changes. For example, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged` is emitted whenever items of data made available by the model are changed. Changes to the headers supplied by the model cause :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerDataChanged` to be emitted. If the structure of the underlying data changes, the model can emit :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutChanged` to indicate to any attached views that they should redisplay any items shown, taking the new structure into account.

The items available through the model can be searched for particular data using the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.match` function.

To sort the model, you can use :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.sort`.

.. _qabstractitemmodel-subclassing:

Subclassing
-----------

**Note:** Some general guidelines for subclassing models are available in the `Model Subclassing Reference <https://doc.qt.io/qt-6/model-view-programming.html#model-subclassing-reference>`_.

When subclassing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, at the very least you must implement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.index`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.parent`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowCount`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.columnCount`, and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`. These functions are used in all read-only models, and form the basis of editable models.

You can also reimplement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.hasChildren` to provide special behavior for models where the implementation of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowCount` is expensive. This makes it possible for models to restrict the amount of data requested by views, and can be used as a way to implement lazy population of model data.

To enable editing in your model, you must also implement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData`, and reimplement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.flags` to ensure that ``ItemIsEditable`` is returned. You can also reimplement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerData` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setHeaderData` to control the way the headers for your model are presented.

The :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerDataChanged` signals must be emitted explicitly when reimplementing the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setHeaderData` functions, respectively.

Custom models need to create model indexes for other components to use. To do this, call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.createIndex` with suitable row and column numbers for the item, and an identifier for it, either as a pointer or as an integer value. The combination of these values must be unique for each item. Custom models typically use these unique identifiers in other reimplemented functions to retrieve item data and access information about the item's parents and children. See the `Simple Tree Model Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-simpletreemodel-example.html>`_ for more information about unique identifiers.

It is not necessary to support every role defined in :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`. Depending on the type of data contained within a model, it may only be useful to implement the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data` function to return valid information for some of the more common roles. Most models provide at least a textual representation of item data for the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`, and well-behaved models should also provide valid information for the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.ToolTipRole` and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.WhatsThisRole`. Supporting these roles enables models to be used with standard Qt views. However, for some models that handle highly-specialized data, it may be appropriate to provide data only for user-defined roles.

Models that provide interfaces to resizable data structures can provide implementations of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns`,and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumns`. When implementing these functions, it is important to notify any connected views about changes to the model's dimensions both *before* and *after* they occur:

* An :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertRows` implementation must call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertRows` *before* inserting new rows into the data structure, and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endInsertRows` *immediately afterwards*.

* An :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns` implementation must call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertColumns` *before* inserting new columns into the data structure, and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endInsertColumns` *immediately afterwards*.

* A :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows` implementation must call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveRows` *before* the rows are removed from the data structure, and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endRemoveRows` *immediately afterwards*.

* A :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumns` implementation must call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveColumns` *before* the columns are removed from the data structure, and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endRemoveColumns` *immediately afterwards*.

The *private* signals that these functions emit give attached components the chance to take action before any data becomes unavailable. The encapsulation of the insert and remove operations with these begin and end functions also enables the model to manage :sip:ref:`~PyQt6.QtCore.QPersistentModelIndex` correctly. **If you want selections to be handled properly, you must ensure that you call these functions.** If you insert or remove an item with children, you do not need to call these functions for the child items. In other words, the parent item will take care of its child items.

To create models that populate incrementally, you can reimplement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.canFetchMore`. If the reimplementation of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore` adds rows to the model, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertRows` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endInsertRows` must be called.

.. seealso:: `Model Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-classes>`_, `Model Subclassing Reference <https://doc.qt.io/qt-6/model-view-programming.html#model-subclassing-reference>`_, :sip:ref:`~PyQt6.QtCore.QModelIndex`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`, `Using drag and drop with item views <https://doc.qt.io/qt-6/model-view-programming.html#using-drag-and-drop-with-item-views>`_, `Simple Tree Model Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-simpletreemodel-example.html>`_, `Editable Tree Model Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-editabletreemodel-example.html>`_, `Fetch More Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-fetchmore-example.html>`_.
