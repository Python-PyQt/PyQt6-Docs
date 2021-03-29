.. sip:method-description::
    :status: todo
    :pysig: eba4956196cd20b697eab7612d06a13b
    :realsig: (int,Qt::SortOrder)
    :digest: ed2aea35634a063a8ec628b4303789cd

Sets the sort indicator for the section specified by the given *logicalIndex* in the direction specified by *order*, and removes the sort indicator from any other section that was showing it.

*logicalIndex* may be -1, in which case no sort indicator will be shown and the model will return to its natural, unsorted order. Note that not all models support this and may even crash in this case.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sortIndicatorSection`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sortIndicatorOrder`.
