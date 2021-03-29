.. sip:signal-description::
    :status: todo
    :pysig: df49685425a6527db499a7680e4bf2ae
    :realsig: (const QList<QPersistentModelIndex>&,QAbstractItemModel::LayoutChangeHint)
    :digest: af0055fac8cde8371dd7642148929e93

This signal is emitted just before the layout of a model is changed. Components connected to this signal use it to adapt to changes in the model's layout.

Subclasses should update any persistent model indexes after emitting .

The optional *parents* parameter is used to give a more specific notification about what parts of the layout of the model are changing. An empty list indicates a change to the layout of the entire model. The order of elements in the *parents* list is not significant. The optional *hint* parameter is used to give a hint about what is happening while the model is relayouting.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutChanged`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.changePersistentIndex`.
