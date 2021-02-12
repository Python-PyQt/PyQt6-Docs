.. sip:method-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: c904c139da39ab7963e512fdaa09a9fe

Begins a column removal operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumns` in a subclass, you must call this function *before* removing data from the model's underlying data store.

The *parent* index corresponds to the parent from which the new columns are removed; *first* and *last* are the column numbers of the first and last columns to be removed.

+--------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| |image-modelview-begin-remove-columns-png| | Specify the first and last column numbers for the span of columns you want to remove from an item in a model.                 |
|                                            |                                                                                                                               |
|                                            | For example, as shown in the diagram, we remove the three columns from column 4 to column 6, so *first* is 4 and *last* is 6: |
|                                            |                                                                                                                               |
|                                            | .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py           |
|                                            |     :lines: 79-79                                                                                                             |
+--------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

**Note:** This function emits the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.columnsAboutToBeRemoved` signal which connected views (or proxies) must handle before the data is removed. Otherwise, the views may end up in an invalid state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endRemoveColumns`.

.. |image-modelview-begin-remove-columns-png| image:: ../../../images/modelview-begin-remove-columns.png
