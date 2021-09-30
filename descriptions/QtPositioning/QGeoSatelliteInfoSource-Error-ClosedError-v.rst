.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 3b4542e6b8b97f0f2663b632484348a4

The satellite backend closed the connection, which happens for example in case the user is switching location services to off. This object becomes invalid and should be deleted. A new satellite source can be created by calling :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.createDefaultSource` later on.
