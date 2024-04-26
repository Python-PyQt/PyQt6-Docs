.. sip:method-description::
    :status: todo
    :pysig: 19033aefa537b4a4de11b07fb9dc6bf9
    :realsig: ()
    :digest: 63bcb26635d265df44916a75ffa510cf

Returns a :sip:ref:`~PyQt6.QtCore.QTimeZone` object that describes local system time.

This method is only available when feature ``timezone`` is enabled. The returned instance is usually equivalent to the lightweight time representation ``QTimeZone(QTimeZone::LocalTime)``, albeit implemented as a time zone.

The returned object will not change to reflect any subsequent change to the system time zone. It represents the local time that was in effect when :sip:ref:`~PyQt6.QtCore.QTimeZone.asBackendZone` was called. On misconfigured systems, such as those that lack the timezone data relied on by the backend for which Qt was compiled, it may be invalid. In such a case, a warning is output.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.utc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.Initialization`, :sip:ref:`~PyQt6.QtCore.QTimeZone.asBackendZone`, :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZoneId`.
