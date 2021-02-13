.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 188c76513a35b1375d016736ec6f1814

Resizes the given *column* based on the size hints of the delegate used to render each item in the column.

**Note:** Only visible columns will be resized. Reimplement :sip:ref:`~PyQt6.QtWidgets.QTableView.sizeHintForColumn` to resize hidden columns as well.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableView.resizeColumnsToContents`, :sip:ref:`~PyQt6.QtWidgets.QTableView.sizeHintForColumn`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.resizeContentsPrecision`.
