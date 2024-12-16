.. sip:method-description::
    :status: todo
    :pysig: 95bc3d14303f22e358f6ff12558385a3
    :realsig: ()
    :digest: ba8f9ec5d5e8a6dcdbb9553a454136df

Returns a list of all available IANA time zone IDs on this system.

This method is only available when feature ``timezone`` is enabled.

**Note:** the :sip:ref:`~PyQt6.QtCore.QTimeZone` constructor will also accept some UTC-offset IDs that are not in the list returned - it would be impractical to list all possible UTC-offset IDs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.isTimeZoneIdAvailable`.
