.. sip:method-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: d49afdbd172981a7915039efc4473953

Begins a row removal operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows` in a subclass, you must call this function *before* removing data from the model's underlying data store.

The *parent* index corresponds to the parent from which the new rows are removed; *first* and *last* are the row numbers of the rows to be removed.

+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| |image-modelview-begin-remove-rows-png| | Specify the first and last row numbers for the span of rows you want to remove from an item in a model.             |
|                                         |                                                                                                                     |
|                                         | For example, as shown in the diagram, we remove the two rows from row 2 to row 3, so *first* is 2 and *last* is 3:  |
|                                         |                                                                                                                     |
|                                         | .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py |
|                                         |     :lines: 64-64                                                                                                   |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------+

**Note:** This function emits the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowsAboutToBeRemoved` signal which connected views (or proxies) must handle before the data is removed. Otherwise, the views may end up in an invalid state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endRemoveRows`.

.. |image-modelview-begin-remove-rows-png| image:: ../../../images/modelview-begin-remove-rows.png
