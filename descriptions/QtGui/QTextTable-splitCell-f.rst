.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int,int,int,int)
    :digest: 7b377d17b24c5463fdc9aa733e457183

Splits the specified cell at *row* and *column* into an array of multiple cells with dimensions specified by *numRows* and *numCols*.

**Note:** It is only possible to split cells that span multiple rows or columns, such as rows that have been merged using :sip:ref:`~PyQt6.QtGui.QTextTable.mergeCells`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTable.mergeCells`.
