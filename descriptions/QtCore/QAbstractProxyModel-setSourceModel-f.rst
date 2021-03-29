.. sip:method-description::
    :status: todo
    :pysig: b1398307ea89da5fe868fb6740f9bc55
    :realsig: (QAbstractItemModel*)
    :digest: 40d4a79d6505bc9452e351598da6f80b

Sets the given *sourceModel* to be processed by the proxy model.

Subclasses should call beginResetModel() at the beginning of the method, disconnect from the old model, call this method, connect to the new model, and call endResetModel().

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel.sourceModel`.
