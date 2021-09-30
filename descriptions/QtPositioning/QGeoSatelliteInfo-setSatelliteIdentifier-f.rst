.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: dc691fcef5cb8cd656f6325cf4b46229

Sets the satellite identifier number to *satId*.

The satellite identifier number can be used to identify a satellite within the satellite system.

The actual value may vary, depending on the platform and the selected backend.

For example, if *nmea* plugin is used, the satellite identifier for GPS satellite system represents the PRN (Pseudo-random noise) number, and the satellite identifier for GLONASS satellite system represents the slot number.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo.satelliteIdentifier`.
