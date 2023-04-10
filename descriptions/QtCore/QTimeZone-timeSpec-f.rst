.. sip:method-description::
    :status: todo
    :pysig: 41145246d08568577980f08c1fee338e
    :realsig: () const
    :digest: 2c79c2638cb47422b449e66b8eeb0453

Returns a :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` identifying the type of time representation.

If the result is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`, this time description is a time zone (backed by system-supplied or standard data); otherwise, it is a lightweight time representation. If the result is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` it describes local time: see :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` for details.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.fixedSecondsAheadOfUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.asBackendZone`.
