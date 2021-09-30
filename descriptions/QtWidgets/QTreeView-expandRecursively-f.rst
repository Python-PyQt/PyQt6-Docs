.. sip:method-description::
    :status: todo
    :pysig: 26719785a098fe9ae286b973ebc17302
    :realsig: (const QModelIndex&,int)
    :digest: 4939096625c1ed12b5831a8ee7635ba3

Expands the item at the given *index* and all its children to the given *depth*. The *depth* is relative to the given *index*. A *depth* of -1 will expand all children, a *depth* of 0 will only expand the given *index*.

**Note:** This function will not try to :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.fetchMore` data.

**Warning:** If the model contains a large number of items, this function will take some time to execute.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeView.expandAll`.
