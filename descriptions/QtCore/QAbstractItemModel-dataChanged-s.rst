.. sip:signal-description::
    :status: todo
    :pysig: 28019a57f7648f93372af030e53c2c9e
    :realsig: (const QModelIndex&,const QModelIndex&,const QList<int>&)
    :digest: 7c2f50bd7d38aa8e99f70b1371f66be0

This signal is emitted whenever the data in an existing item changes.

If the items are of the same parent, the affected ones are those between *topLeft* and *bottomRight* inclusive. If the items do not have the same parent, the behavior is undefined.

When reimplementing the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData` function, this signal must be emitted explicitly.

The optional *roles* argument can be used to specify which data roles have actually been modified. An empty vector in the roles argument means that all roles should be considered modified. The order of elements in the roles argument does not have any relevance.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerDataChanged`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutChanged`.
