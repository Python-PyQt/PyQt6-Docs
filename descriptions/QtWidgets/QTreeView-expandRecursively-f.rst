.. sip:method-description::
    :status: todo
    :pysig: 26719785a098fe9ae286b973ebc17302
    :realsig: (const QModelIndex&,int)
    :digest: 33107e2d4abb065b103bd7b1a9833d63

Expands the item at the given *index* and all its children to the given *depth*. The *depth* is relative to the given *index*. A *depth* of -1 will expand all children, a *depth* of 0 will only expand the given *index*.

**Warning:** : if the model contains a large number of items, this function will take some time to execute.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeView.expandAll`.
