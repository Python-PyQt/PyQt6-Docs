.. sip:method-description::
    :status: todo
    :pysig: ffb5c77f6be2ae0d97654825b3b60e67
    :realsig: (int) const
    :digest: 7dde240ec885c1816c8e2dcc21e081ac

Returns a :sip:ref:`~PyQt6.QtCore.QTime` object containing a time *s* seconds later than the time of this object (or earlier if *s* is negative).

Note that the time will wrap if it passes midnight.

Returns a null time if this time is invalid.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 91-96

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.addMSecs`, :sip:ref:`~PyQt6.QtCore.QTime.secsTo`, :sip:ref:`~PyQt6.QtCore.QDateTime.addSecs`.
