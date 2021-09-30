.. sip:method-description::
    :status: todo
    :pysig: 0989359b83eed7ee431a6e458e8a8bc8
    :realsig: (const char*,int,QList<QGeoSatelliteInfo>&,QGeoSatelliteInfo::SatelliteSystem&)
    :digest: e3eaf61f88a290012b498a8b0be693f7

Parses an NMEA sentence string to extract the information about satellites in view.

The default implementation will parse standard NMEA $GPGSV sentences. This method should be reimplemented in a subclass whenever the need to deal with non-standard NMEA sentences arises.

The parser reads *size* bytes from *data* and uses that information to fill *infos* list.

Returns :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus.SatelliteInfoParseStatus` with parse result. Modifies *infos* list in case :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus.PartiallyParsed` or :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus.FullyParsed` is returned. Also sets the *system* to correct satellite system type. This is required to determine the system type in case there are no satellites in view.
