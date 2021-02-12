.. sip:signal-description::
    :status: todo
    :pysig: df49685425a6527db499a7680e4bf2ae
    :realsig: (const QList<QPersistentModelIndex>&,QAbstractItemModel::LayoutChangeHint)
    :digest: 4ebb25a875de63d24e2cff42196d13c5

This signal is emitted whenever the layout of items exposed by the model has changed; for example, when the model has been sorted. When this signal is received by a view, it should update the layout of items to reflect this change.

When subclassing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` or :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`, ensure that you emit :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutAboutToBeChanged` before changing the order of items or altering the structure of the data you expose to views, and emit  after changing the layout.

The optional *parents* parameter is used to give a more specific notification about what parts of the layout of the model are changing. An empty list indicates a change to the layout of the entire model. The order of elements in the *parents* list is not significant. The optional *hint* parameter is used to give a hint about what is happening while the model is relayouting.

Subclasses should update any persistent model indexes before emitting . In other words, when the structure changes:

* emit :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutAboutToBeChanged`

* Remember the :sip:ref:`~PyQt6.QtCore.QModelIndex` that will change

* Update your internal data

* Call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.changePersistentIndex`

* emit

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutAboutToBeChanged`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerDataChanged`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelReset`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.changePersistentIndex`.
