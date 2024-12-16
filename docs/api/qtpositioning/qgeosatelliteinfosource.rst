:orphan:

.. sip:class:: PyQt6.QtPositioning.QGeoSatelliteInfoSource
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtPositioning/QGeoSatelliteInfoSource-c.rst

    .. sip:enum:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error
        :description: QtPositioning/QGeoSatelliteInfoSource-Error-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error.AccessError
            :description: QtPositioning/QGeoSatelliteInfoSource-Error-AccessError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error.ClosedError
            :description: QtPositioning/QGeoSatelliteInfoSource-Error-ClosedError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error.NoError
            :description: QtPositioning/QGeoSatelliteInfoSource-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error.UnknownSourceError
            :description: QtPositioning/QGeoSatelliteInfoSource-Error-UnknownSourceError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error.UpdateTimeoutError
            :description: QtPositioning/QGeoSatelliteInfoSource-Error-UpdateTimeoutError-v.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtPositioning/QGeoSatelliteInfoSource-__init__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.availableSources
        :returns:
            list[str]
        :static:
        :description: QtPositioning/QGeoSatelliteInfoSource-availableSources-f-1.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.backendProperty
        :args:
            Optional[str]
        :returns:
            Any
        :description: QtPositioning/QGeoSatelliteInfoSource-backendProperty-f-1.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.createDefaultSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource`
        :static:
        :description: QtPositioning/QGeoSatelliteInfoSource-createDefaultSource-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.createDefaultSource
        :args:
            dict[Optional[str], Any]
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource`
        :static:
        :description: QtPositioning/QGeoSatelliteInfoSource-createDefaultSource-f-1.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.createSource
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource`
        :static:
        :description: QtPositioning/QGeoSatelliteInfoSource-createSource-f-2.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.createSource
        :args:
            Optional[str]
            dict[Optional[str], Any]
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource`
        :static:
        :description: QtPositioning/QGeoSatelliteInfoSource-createSource-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.error
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error`
        :description: QtPositioning/QGeoSatelliteInfoSource-error-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.minimumUpdateInterval
        :returns:
            int
        :description: QtPositioning/QGeoSatelliteInfoSource-minimumUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.requestUpdate
        :args:
            timeout: int = 0
        :description: QtPositioning/QGeoSatelliteInfoSource-requestUpdate-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.setBackendProperty
        :args:
            Optional[str]
            Any
        :returns:
            bool
        :description: QtPositioning/QGeoSatelliteInfoSource-setBackendProperty-f-1.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.setUpdateInterval
        :args:
            int
        :description: QtPositioning/QGeoSatelliteInfoSource-setUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.sourceName
        :returns:
            str
        :description: QtPositioning/QGeoSatelliteInfoSource-sourceName-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.startUpdates
        :description: QtPositioning/QGeoSatelliteInfoSource-startUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.stopUpdates
        :description: QtPositioning/QGeoSatelliteInfoSource-stopUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.updateInterval
        :returns:
            int
        :description: QtPositioning/QGeoSatelliteInfoSource-updateInterval-f.rst

    .. sip:signal:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error`
        :description: QtPositioning/QGeoSatelliteInfoSource-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.satellitesInUseUpdated
        :args:
            Iterable[:sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo`]
        :description: QtPositioning/QGeoSatelliteInfoSource-satellitesInUseUpdated-s.rst

    .. sip:signal:: PyQt6.QtPositioning.QGeoSatelliteInfoSource.satellitesInViewUpdated
        :args:
            Iterable[:sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo`]
        :description: QtPositioning/QGeoSatelliteInfoSource-satellitesInViewUpdated-s.rst
