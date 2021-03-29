.. sip:method-description::
    :status: todo
    :pysig: 64057e5a182ab705ccb12c2b1f2a0b03
    :realsig: () const
    :digest: 8024223ed0ff24ca9fb0bef91acf5810

Returns the time zone of the datetime.

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` then an instance of the current system time zone will be returned. Note however that if you copy this time zone the instance will not remain in sync if the system time zone changes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`, :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`.
