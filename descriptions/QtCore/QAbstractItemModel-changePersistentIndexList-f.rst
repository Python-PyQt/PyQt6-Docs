.. sip:method-description::
    :status: todo
    :pysig: 10bf0b84706dc0485f3890fb27b0c1f4
    :realsig: (const QModelIndexList&,const QModelIndexList&)
    :digest: 39ae728a6222fd9b61b7092ef45d2a7a

Changes the {\ :sip:ref:`~PyQt6.QtCore.QPersistentModelIndex`}es that are equal to the indexes in the given *from* model index list to the given *to* model index list.

If no persistent model indexes equal to the indexes in the given *from* model index list are found, nothing is changed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.persistentIndexList`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.changePersistentIndex`.
