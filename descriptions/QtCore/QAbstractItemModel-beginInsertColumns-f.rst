.. sip:method-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: 03be28d394b4355ab1aa41b85f2286af

Begins a column insertion operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns` in a subclass, you must call this function *before* inserting data into the model's underlying data store.

The *parent* index corresponds to the parent into which the new columns are inserted; *first* and *last* are the column numbers of the new columns will have after they have been inserted.

+--------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-modelview-begin-insert-columns-png| | Specify the first and last column numbers for the span of columns you want to insert into an item in a model.                                                |
|                                            |                                                                                                                                                              |
|                                            | For example, as shown in the diagram, we insert three columns before column 4, so *first* is 4 and *last* is 6:                                              |
|                                            |                                                                                                                                                              |
|                                            | .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py                                          |
|                                            |     :lines: 69-69                                                                                                                                            |
|                                            |                                                                                                                                                              |
|                                            | This inserts the three new columns as columns 4, 5, and 6.                                                                                                   |
+--------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-modelview-begin-append-columns-png| | To append columns, insert them after the last column.                                                                                                        |
|                                            |                                                                                                                                                              |
|                                            | For example, as shown in the diagram, we append three columns to a collection of six existing columns (ending in column 5), so *first* is 6 and *last* is 8: |
|                                            |                                                                                                                                                              |
|                                            | .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py                                          |
|                                            |     :lines: 74-74                                                                                                                                            |
|                                            |                                                                                                                                                              |
|                                            | This appends the two new columns as columns 6, 7, and 8.                                                                                                     |
+--------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** This function emits the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.columnsAboutToBeInserted` signal which connected views (or proxies) must handle before the data is inserted. Otherwise, the views may end up in an invalid state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endInsertColumns`.

.. |image-modelview-begin-insert-columns-png| image:: ../../../images/modelview-begin-insert-columns.png
.. |image-modelview-begin-append-columns-png| image:: ../../../images/modelview-begin-append-columns.png
