.. sip:method-description::
    :status: todo
    :pysig: db2bb5be90d937c1e40ba29e1d1a36d3
    :realsig: (QDate, QDateTime::TransitionResolution)
    :digest: c6fc5357eb2fd6a08b652db58634462f

Sets the date part of this datetime to *date*.

If no time is set yet, it is set to midnight. If *date* is invalid, this :sip:ref:`~PyQt6.QtCore.QDateTime` becomes invalid.

If *date* and :sip:ref:`~PyQt6.QtCore.QDateTime.time` describe a moment close to a transition for this datetime's time representation, *resolve* controls how that situation is resolved.

**Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.date`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTime`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`.
