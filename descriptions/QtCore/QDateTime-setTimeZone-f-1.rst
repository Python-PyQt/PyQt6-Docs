.. sip:method-description::
    :status: todo
    :pysig: bba7fe9246da261144be13cef463b119
    :realsig: (const QTimeZone&, QDateTime::TransitionResolution)
    :digest: 8544e562d8ce8289504ec212c9620c0b

Sets the time zone used in this datetime to *toZone*.

The datetime may refer to a different point in time. It uses the time representation of *toZone*, which may change the meaning of its unchanged :sip:ref:`~PyQt6.QtCore.QDateTime.date` and :sip:ref:`~PyQt6.QtCore.QDateTime.time`.

If *toZone* is invalid then the datetime will be invalid. Otherwise, this datetime's :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` after the call will match ``toZone.timeSpec()``.

If :sip:ref:`~PyQt6.QtCore.QDateTime.date` and :sip:ref:`~PyQt6.QtCore.QDateTime.time` describe a moment close to a transition for *toZone*, *resolve* controls how that situation is resolved.

**Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeRepresentation`, :sip:ref:`~PyQt6.QtCore.QDateTime.timeZone`, :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`.
