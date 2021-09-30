:orphan:

.. sip:class:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource
    :inherits: :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource`
    :description: QtPositioning/QNmeaSatelliteInfoSource-c.rst

    .. sip:enum:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus
        :description: QtPositioning/QNmeaSatelliteInfoSource-SatelliteInfoParseStatus-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus.FullyParsed
            :description: QtPositioning/QNmeaSatelliteInfoSource-SatelliteInfoParseStatus-FullyParsed-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus.NotParsed
            :description: QtPositioning/QNmeaSatelliteInfoSource-SatelliteInfoParseStatus-NotParsed-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus.PartiallyParsed
            :description: QtPositioning/QNmeaSatelliteInfoSource-SatelliteInfoParseStatus-PartiallyParsed-v.rst

    .. sip:enum:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode
        :description: QtPositioning/QNmeaSatelliteInfoSource-UpdateMode-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode.RealTimeMode
            :description: QtPositioning/QNmeaSatelliteInfoSource-UpdateMode-RealTimeMode-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode.SimulationMode
            :description: QtPositioning/QNmeaSatelliteInfoSource-UpdateMode-SimulationMode-v.rst

    .. sip:attribute:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SimulationUpdateInterval
        :type: str
        :static:
        :description: QtPositioning/QNmeaSatelliteInfoSource-SimulationUpdateInterval-a.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.__init__
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtPositioning/QNmeaSatelliteInfoSource-__init__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.backendProperty
        :args:
            str
        :returns:
            Any
        :description: QtPositioning/QNmeaSatelliteInfoSource-backendProperty-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtPositioning/QNmeaSatelliteInfoSource-device-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.error
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.Error`
        :description: QtPositioning/QNmeaSatelliteInfoSource-error-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.minimumUpdateInterval
        :returns:
            int
        :description: QtPositioning/QNmeaSatelliteInfoSource-minimumUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.parseSatelliteInfoFromNmea
        :args:
            str
            int
            Iterable[:sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo`]
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus`
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem`
        :description: QtPositioning/QNmeaSatelliteInfoSource-parseSatelliteInfoFromNmea-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.parseSatellitesInUseFromNmea
        :args:
            str
            int
            Iterable[int]
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem`
        :description: QtPositioning/QNmeaSatelliteInfoSource-parseSatellitesInUseFromNmea-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.requestUpdate
        :args:
            timeout: int = 0
        :description: QtPositioning/QNmeaSatelliteInfoSource-requestUpdate-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.setBackendProperty
        :args:
            str
            Any
        :returns:
            bool
        :description: QtPositioning/QNmeaSatelliteInfoSource-setBackendProperty-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtPositioning/QNmeaSatelliteInfoSource-setDevice-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.setUpdateInterval
        :args:
            int
        :description: QtPositioning/QNmeaSatelliteInfoSource-setUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.startUpdates
        :description: QtPositioning/QNmeaSatelliteInfoSource-startUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.stopUpdates
        :description: QtPositioning/QNmeaSatelliteInfoSource-stopUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaSatelliteInfoSource.updateMode
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode`
        :description: QtPositioning/QNmeaSatelliteInfoSource-updateMode-f.rst
