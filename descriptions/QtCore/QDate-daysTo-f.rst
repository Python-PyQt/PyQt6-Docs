.. sip:method-description::
    :status: todo
    :pysig: e48a49a16893a71bf9b5b2a1de49f66f
    :realsig: (QDate) const
    :digest: 067aad06b488ebfd5e7f5c05a5c9d3e5

Returns the number of days from this date to *d* (which is negative if *d* is earlier than this date).

Returns 0 if either date is invalid.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 54-57

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.addDays`.
