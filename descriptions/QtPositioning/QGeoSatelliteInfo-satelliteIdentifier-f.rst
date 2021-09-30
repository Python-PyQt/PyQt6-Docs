.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: c5e57df4d6f8609c5803c79118922475

Returns the satellite identifier number.

The satellite identifier number can be used to identify a satellite within the satellite system.

The actual value may vary, depending on the platform and the selected backend.

For example, if *nmea* plugin is used, the satellite identifier for GPS satellite system represents the PRN (Pseudo-random noise) number, and the satellite identifier for GLONASS satellite system represents the slot number.

For NMEA-based backends the satellite identifier can be used to determine the satellite system type if it is not available from other sources. You can refer to `satellite IDs list <https://gpsd.gitlab.io/gpsd/NMEA.html#_satellite_ids>`_ to check the ID ranges for different satellite systems.

**Note:** Depending on the platform and the selected backend, the satellite identifier ranges for different satellite systems may intersect. To uniquely identify a satellite, a combination of satelliteIndetifier() and :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo.satelliteSystem` must be used.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo.setSatelliteIdentifier`, :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo.satelliteSystem`.
