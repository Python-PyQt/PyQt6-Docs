.. sip:method-description::
    :status: todo
    :pysig: 420f237986cb273ad62d4b2b220a3425
    :realsig: (const char*,int,QList<int>&)
    :digest: 9df95fb39259dc7105ce044572ecabcf

Parses an NMEA sentence string to extract the IDs of satelites in use.

The default implementation will parse standard NMEA $GPGSA sentences. This method should be reimplemented in a subclass whenever the need to deal with non-standard NMEA sentences arises.

The parser reads *size* bytes from *data* and uses that information to fill *pnrsInUse* list.

Returns system type if the sentence was successfully parsed, otherwise returns :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem.Undefined` and should not modifiy *pnrsInUse*.
