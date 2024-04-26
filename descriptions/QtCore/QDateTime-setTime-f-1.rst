.. sip:method-description::
    :status: todo
    :pysig: dc7faa385b7a456dfcdfd9381906c87c
    :realsig: (QTime, QDateTime::TransitionResolution)
    :digest: 202190a6bc33e6578ed38d3e33430bd3

Sets the time part of this datetime to *time*. If *time* is not valid, this function sets it to midnight. Therefore, it's possible to clear any set time in a :sip:ref:`~PyQt6.QtCore.QDateTime` by setting it to a default :sip:ref:`~PyQt6.QtCore.QTime`:

::

    QDateTime dt = QDateTime::currentDateTime();
    dt.setTime(QTime());

If :sip:ref:`~PyQt6.QtCore.QDateTime.date` and *time* describe a moment close to a transition for this datetime's time representation, *resolve* controls how that situation is resolved.

**Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.time`, :sip:ref:`~PyQt6.QtCore.QDateTime.setDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`.
