.. sip:method-description::
    :status: todo
    :pysig: 42596ea490c991d4e66a720720162ea5
    :realsig: (QTime) const
    :digest: 621f9ceee3fa6b090a35daee3bb8c913

Returns the number of milliseconds from this time to *t*. If *t* is earlier than this time, the number of milliseconds returned is negative.

Because :sip:ref:`~PyQt6.QtCore.QTime` measures time within a day and there are 86400 seconds in a day, the result is always between -86400000 and 86400000 ms.

Returns 0 if either time is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.secsTo`, :sip:ref:`~PyQt6.QtCore.QTime.addMSecs`, :sip:ref:`~PyQt6.QtCore.QDateTime.msecsTo`.
