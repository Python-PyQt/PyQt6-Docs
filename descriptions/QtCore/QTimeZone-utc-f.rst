.. sip:method-description::
    :status: todo
    :pysig: 19033aefa537b4a4de11b07fb9dc6bf9
    :realsig: ()
    :digest: 86e78d55753950c9d4dce242176da483

Returns a :sip:ref:`~PyQt6.QtCore.QTimeZone` object that describes UTC as a time zone.

This method is only available when feature ``timezone`` is enabled. It is equivalent to passing 0 to :sip:ref:`~PyQt6.QtCore.QTimeZone`\ (int offsetSeconds) and to the lightweight time representation :sip:ref:`~PyQt6.QtCore.QTimeZone`\ (\ :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC`), albeit implemented as a time zone, unlike the latter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone`, :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.Initialization`, :sip:ref:`~PyQt6.QtCore.QTimeZone.asBackendZone`.
