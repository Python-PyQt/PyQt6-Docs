.. sip:method-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: 80dee5e0a4f921ecbc94c04dda9db3af

This slot is called when rows are inserted. The new rows are those under the given *parent* from *start* to *end* inclusive. The base class implementation calls fetchMore() on the model to check for more data.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.rowsAboutToBeRemoved`.
