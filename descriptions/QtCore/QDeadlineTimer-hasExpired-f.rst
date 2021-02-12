.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: a7b8e17261b2401906683c4c23cc39f8

Returns true if this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object has expired, false if there remains time left. For objects that have expired, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime` will return zero and :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` will return a time point in the past.

:sip:ref:`~PyQt6.QtCore.QDeadlineTimer` objects created with the :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.ForeverConstant.ForeverConstant` never expire and this function always returns false for them.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`.
