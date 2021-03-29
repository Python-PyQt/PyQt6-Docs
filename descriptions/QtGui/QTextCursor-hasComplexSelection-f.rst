.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 0cffdb0b32dd6d14bf46e7d19afc9cd7

Returns ``true`` if the cursor contains a selection that is not simply a range from :sip:ref:`~PyQt6.QtGui.QTextCursor.selectionStart` to :sip:ref:`~PyQt6.QtGui.QTextCursor.selectionEnd`; otherwise returns ``false``.

Complex selections are ones that span at least two cells in a table; their extent is specified by :sip:ref:`~PyQt6.QtGui.QTextCursor.selectedTableCells`.
