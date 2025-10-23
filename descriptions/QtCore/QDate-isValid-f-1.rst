.. sip:method-description::
    :status: todo
    :pysig: 58375a5c171c9a9707c491645f766cdf
    :realsig: (int,int,int)
    :digest: 03c772042b03af52ffbb706ea0644a70

Returns ``true`` if the specified date (\ *year*, *month*, and *day*) is valid in the Gregorian calendar; otherwise returns ``false``.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 80-86

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.isNull`, :sip:ref:`~PyQt6.QtCore.QDate.setDate`, :sip:ref:`~PyQt6.QtCore.QCalendar.isDateValid`.
