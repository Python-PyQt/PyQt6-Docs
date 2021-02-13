.. sip:class-description::
    :status: todo
    :brief: Base class for proxy item models that can do sorting, filtering or other data processing tasks
    :digest: 38201d0d57d4ff8e4a069a14a4b86abd

The :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel` class provides a base class for proxy item models that can do sorting, filtering or other data processing tasks.

This class defines the standard interface that proxy models must use to be able to interoperate correctly with other model/view components. It is not supposed to be instantiated directly.

All standard proxy models are derived from the :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel` class. If you need to create a new proxy model class, it is usually better to subclass an existing class that provides the closest behavior to the one you want to provide.

Proxy models that filter or sort items of data from a source model should be created by using or subclassing :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel`.

To subclass :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`, you need to implement :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel.mapFromSource` and :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel.mapToSource`. The :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel.mapSelectionFromSource` and :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel.mapSelectionToSource` functions only need to be reimplemented if you need a behavior different from the default behavior.

**Note:** If the source model is deleted or no source model is specified, the proxy model operates on a empty placeholder model.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.
