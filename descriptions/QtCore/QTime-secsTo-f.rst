.. sip:method-description::
    :status: todo
    :pysig: 42596ea490c991d4e66a720720162ea5
    :realsig: (QTime) const
    :digest: c5941102eeb997d3643d0cb570b0679c

Returns the number of seconds from this time to *t*. If *t* is earlier than this time, the number of seconds returned is negative.

Because :sip:ref:`~PyQt6.QtCore.QTime` measures time within a day and there are 86400 seconds in a day, the result is always between -86400 and 86400.

does not take into account any milliseconds.

Returns 0 if either time is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.addSecs`, :sip:ref:`~PyQt6.QtCore.QDateTime.secsTo`.
