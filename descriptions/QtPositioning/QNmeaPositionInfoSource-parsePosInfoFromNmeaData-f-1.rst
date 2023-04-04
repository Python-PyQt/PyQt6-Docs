.. sip:method-description::
    :status: todo
    :pysig: ec7e0b09a1c08eaa1a6e4a2b0540f758
    :realsig: (const char*,int,QGeoPositionInfo*,bool*)
    :digest: 79f3fd93ee0d4b3146bce764eeebf096

Parses an NMEA sentence string into a :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfo`.

The default implementation will parse standard NMEA sentences. This method should be reimplemented in a subclass whenever the need to deal with non-standard NMEA sentences arises.

The parser reads *size* bytes from *data* and uses that information to setup *posInfo* and *hasFix*. If *hasFix* is set to false then *posInfo* may contain only the time or the date and the time.

Returns true if the sentence was successfully parsed, otherwise returns false and should not modifiy *posInfo* or *hasFix*.
