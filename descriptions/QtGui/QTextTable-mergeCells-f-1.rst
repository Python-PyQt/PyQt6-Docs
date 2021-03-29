.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int,int,int,int)
    :digest: 04de0d08c2960de2f71e579eb4c76804

Merges the cell at the specified *row* and *column* with the adjacent cells into one cell. The new cell will span *numRows* rows and *numCols* columns. This method does nothing if *numRows* or *numCols* is less than the current number of rows or columns spanned by the cell.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTable.splitCell`.
