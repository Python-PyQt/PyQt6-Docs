.. sip:method-description::
    :status: todo
    :pysig: 6e60578a215cfb6c006cca2a9d60e308
    :realsig: (const QTextCharFormat&)
    :digest: f980df6d577b740f87518f5d3d8ab47a

Sets the cell's character format to *format*. This can for example be used to change the background color of the entire cell:

:sip:ref:`~PyQt6.QtGui.QTextTableCell` cell = table->cellAt(2, 3); :sip:ref:`~PyQt6.QtGui.QTextCharFormat` format = cell.\ :sip:ref:`~PyQt6.QtGui.QTextTableCell.format`; format.setBackground(\ :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.blue`); cell.(format);

Note that the cell's row or column span cannot be changed through this function. You have to use :sip:ref:`~PyQt6.QtGui.QTextTable.mergeCells` and :sip:ref:`~PyQt6.QtGui.QTextTable.splitCell` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTableCell.format`.
