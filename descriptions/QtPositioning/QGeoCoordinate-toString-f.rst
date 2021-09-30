.. sip:method-description::
    :status: todo
    :pysig: 9233b37fa18b017bb919d530476e38c7
    :realsig: (QGeoCoordinate::CoordinateFormat) const
    :digest: f6563a95e4c6621d43867e322f12a10f

Returns this coordinate as a string in the specified *format*.

For example, if this coordinate has a latitude of -27.46758, a longitude of 153.027892 and an altitude of 28.1, these are the strings returned depending on *format*:

+-----------------------------------------------------------------------------------------------------+----------------------------------------+
| *format* value                                                                                      | Returned string                        |
+=====================================================================================================+========================================+
| :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.Degrees`                             | -27.46758°, 153.02789°, 28.1m          |
+-----------------------------------------------------------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesWithHemisphere`               | 27.46758° S, 153.02789° E, 28.1m       |
+-----------------------------------------------------------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutes`                      | -27° 28.054', 153° 1.673', 28.1m       |
+-----------------------------------------------------------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesWithHemisphere`        | 27° 28.054 S', 153° 1.673' E, 28.1m    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSeconds`               | -27° 28' 3.2", 153° 1' 40.4", 28.1m    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSecondsWithHemisphere` | 27° 28' 3.2" S, 153° 1' 40.4" E, 28.1m |
+-----------------------------------------------------------------------------------------------------+----------------------------------------+

The altitude field is omitted if no altitude is set.

If the coordinate is invalid, an empty string is returned.
