.. sip:method-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: 1b31a0e64f005727e58b32829d0da471

Begins a row insertion operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertRows` in a subclass, you must call this function *before* inserting data into the model's underlying data store.

The *parent* index corresponds to the parent into which the new rows are inserted; *first* and *last* are the row numbers that the new rows will have after they have been inserted.

+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-modelview-begin-insert-rows-png| | Specify the first and last row numbers for the span of rows you want to insert into an item in a model.                                         |
|                                         |                                                                                                                                                 |
|                                         | For example, as shown in the diagram, we insert three rows before row 2, so *first* is 2 and *last* is 4:                                       |
|                                         |                                                                                                                                                 |
|                                         | .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py                             |
|                                         |     :lines: 54-54                                                                                                                               |
|                                         |                                                                                                                                                 |
|                                         | This inserts the three new rows as rows 2, 3, and 4.                                                                                            |
+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-modelview-begin-append-rows-png| | To append rows, insert them after the last row.                                                                                                 |
|                                         |                                                                                                                                                 |
|                                         | For example, as shown in the diagram, we append two rows to a collection of 4 existing rows (ending in row 3), so *first* is 4 and *last* is 5: |
|                                         |                                                                                                                                                 |
|                                         | .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py                             |
|                                         |     :lines: 59-59                                                                                                                               |
|                                         |                                                                                                                                                 |
|                                         | This appends the two new rows as rows 4 and 5.                                                                                                  |
+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** This function emits the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowsAboutToBeInserted` signal which connected views (or proxies) must handle before the data is inserted. Otherwise, the views may end up in an invalid state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endInsertRows`.

.. |image-modelview-begin-insert-rows-png| image:: ../../../images/modelview-begin-insert-rows.png
.. |image-modelview-begin-append-rows-png| image:: ../../../images/modelview-begin-append-rows.png
