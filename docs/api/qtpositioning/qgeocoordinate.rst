:orphan:

.. sip:class:: PyQt6.QtPositioning.QGeoCoordinate
    :description: QtPositioning/QGeoCoordinate-c.rst

    .. sip:enum:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat
        :description: QtPositioning/QGeoCoordinate-CoordinateFormat-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.Degrees
            :description: QtPositioning/QGeoCoordinate-CoordinateFormat-Degrees-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutes
            :description: QtPositioning/QGeoCoordinate-CoordinateFormat-DegreesMinutes-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSeconds
            :description: QtPositioning/QGeoCoordinate-CoordinateFormat-DegreesMinutesSeconds-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSecondsWithHemisphere
            :description: QtPositioning/QGeoCoordinate-CoordinateFormat-DegreesMinutesSecondsWithHemisphere-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesWithHemisphere
            :description: QtPositioning/QGeoCoordinate-CoordinateFormat-DegreesMinutesWithHemisphere-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesWithHemisphere
            :description: QtPositioning/QGeoCoordinate-CoordinateFormat-DegreesWithHemisphere-v.rst

    .. sip:enum:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateType
        :description: QtPositioning/QGeoCoordinate-CoordinateType-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateType.Coordinate2D
            :description: QtPositioning/QGeoCoordinate-CoordinateType-Coordinate2D-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateType.Coordinate3D
            :description: QtPositioning/QGeoCoordinate-CoordinateType-Coordinate3D-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoCoordinate.CoordinateType.InvalidCoordinate
            :description: QtPositioning/QGeoCoordinate-CoordinateType-InvalidCoordinate-v.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.__init__
        :description: QtPositioning/QGeoCoordinate-__init__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.__init__
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate`
        :description: QtPositioning/QGeoCoordinate-__init__-f-1.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.__init__
        :args:
            float
            float
        :description: QtPositioning/QGeoCoordinate-__init__-f-2.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.__init__
        :args:
            float
            float
            float
        :description: QtPositioning/QGeoCoordinate-__init__-f-3.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.altitude
        :returns:
            float
        :description: QtPositioning/QGeoCoordinate-altitude-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.atDistanceAndAzimuth
        :args:
            float
            float
            distanceUp: float = 0
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate`
        :description: QtPositioning/QGeoCoordinate-atDistanceAndAzimuth-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.azimuthTo
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate`
        :returns:
            float
        :description: QtPositioning/QGeoCoordinate-azimuthTo-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.distanceTo
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate`
        :returns:
            float
        :description: QtPositioning/QGeoCoordinate-distanceTo-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.__eq__
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate`
        :returns:
            bool
        :description: QtPositioning/QGeoCoordinate-__eq__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.__hash__
        :returns:
            int
        :description: QtPositioning/QGeoCoordinate-__hash__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.isValid
        :returns:
            bool
        :description: QtPositioning/QGeoCoordinate-isValid-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.latitude
        :returns:
            float
        :description: QtPositioning/QGeoCoordinate-latitude-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.longitude
        :returns:
            float
        :description: QtPositioning/QGeoCoordinate-longitude-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.__ne__
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate`
        :returns:
            bool
        :description: QtPositioning/QGeoCoordinate-__ne__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.setAltitude
        :args:
            float
        :description: QtPositioning/QGeoCoordinate-setAltitude-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.setLatitude
        :args:
            float
        :description: QtPositioning/QGeoCoordinate-setLatitude-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.setLongitude
        :args:
            float
        :description: QtPositioning/QGeoCoordinate-setLongitude-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.swap
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate`
        :description: QtPositioning/QGeoCoordinate-swap-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.toString
        :args:
            format: :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat` = :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSecondsWithHemisphere`
        :returns:
            str
        :description: QtPositioning/QGeoCoordinate-toString-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoCoordinate.type
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateType`
        :description: QtPositioning/QGeoCoordinate-type-f.rst
