.. sip:method-description::
    :status: todo
    :pysig: 6e60578a215cfb6c006cca2a9d60e308
    :realsig: (const QTextCharFormat&)
    :digest: e5b4cf6b2624d96b91796814769c3403

Sets the cell's character format to *format*. This can for example be used to change the background color of the entire cell:

::

    QTextTableCell cell = table->cellAt(2, 3);
    QTextCharFormat format = cell.format();
    format.setBackground(Qt::blue);
    cell.setFormat(format);

Note that the cell's row or column span cannot be changed through this function. You have to use :sip:ref:`~PyQt6.QtGui.QTextTable.mergeCells` and :sip:ref:`~PyQt6.QtGui.QTextTable.splitCell` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTableCell.format`.
