.. sip:method-description::
    :status: todo
    :pysig: 19033aefa537b4a4de11b07fb9dc6bf9
    :realsig: ()
    :digest: 42f0fcdf48c698649f85b9dbdcb90b14

Returns a :sip:ref:`~PyQt6.QtCore.QTimeZone` object that describes local system time.

This method is only available when feature ``timezone`` is enabled. The returned instance is usually equivalent to the lightweight time representation ``QTimeZone(QTimeZone::LocalTime)``, albeit implemented as a time zone.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.utc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.Initialization`, :sip:ref:`~PyQt6.QtCore.QTimeZone.asBackendZone`.
