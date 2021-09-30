:orphan:

.. sip:class:: PyQt6.QtPositioning.QGeoPositionInfoSource
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtPositioning/QGeoPositionInfoSource-c.rst

    .. sip:enum:: PyQt6.QtPositioning.QGeoPositionInfoSource.Error
        :description: QtPositioning/QGeoPositionInfoSource-Error-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.Error.AccessError
            :description: QtPositioning/QGeoPositionInfoSource-Error-AccessError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.Error.ClosedError
            :description: QtPositioning/QGeoPositionInfoSource-Error-ClosedError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.Error.NoError
            :description: QtPositioning/QGeoPositionInfoSource-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.Error.UnknownSourceError
            :description: QtPositioning/QGeoPositionInfoSource-Error-UnknownSourceError-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.Error.UpdateTimeoutError
            :description: QtPositioning/QGeoPositionInfoSource-Error-UpdateTimeoutError-v.rst

    .. sip:enum:: PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod
        :description: QtPositioning/QGeoPositionInfoSource-PositioningMethod-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod.AllPositioningMethods
            :description: QtPositioning/QGeoPositionInfoSource-PositioningMethod-AllPositioningMethods-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod.NonSatellitePositioningMethods
            :description: QtPositioning/QGeoPositionInfoSource-PositioningMethod-NonSatellitePositioningMethods-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod.NoPositioningMethods
            :description: QtPositioning/QGeoPositionInfoSource-PositioningMethod-NoPositioningMethods-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod.SatellitePositioningMethods
            :description: QtPositioning/QGeoPositionInfoSource-PositioningMethod-SatellitePositioningMethods-v.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtPositioning/QGeoPositionInfoSource-__init__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.availableSources
        :returns:
            List[str]
        :static:
        :description: QtPositioning/QGeoPositionInfoSource-availableSources-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.backendProperty
        :args:
            str
        :returns:
            Any
        :description: QtPositioning/QGeoPositionInfoSource-backendProperty-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.createDefaultSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource`
        :static:
        :description: QtPositioning/QGeoPositionInfoSource-createDefaultSource-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.createDefaultSource
        :args:
            Dict[str, Any]
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource`
        :static:
        :description: QtPositioning/QGeoPositionInfoSource-createDefaultSource-f-1.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.createSource
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource`
        :static:
        :description: QtPositioning/QGeoPositionInfoSource-createSource-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.createSource
        :args:
            str
            Dict[str, Any]
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource`
        :static:
        :description: QtPositioning/QGeoPositionInfoSource-createSource-f-1.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.error
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.Error`
        :description: QtPositioning/QGeoPositionInfoSource-error-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.lastKnownPosition
        :args:
            fromSatellitePositioningMethodsOnly: bool = False
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfo`
        :description: QtPositioning/QGeoPositionInfoSource-lastKnownPosition-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.minimumUpdateInterval
        :returns:
            int
        :description: QtPositioning/QGeoPositionInfoSource-minimumUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.preferredPositioningMethods
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod`
        :description: QtPositioning/QGeoPositionInfoSource-preferredPositioningMethods-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.requestUpdate
        :args:
            timeout: int = 0
        :description: QtPositioning/QGeoPositionInfoSource-requestUpdate-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.setBackendProperty
        :args:
            str
            Any
        :returns:
            bool
        :description: QtPositioning/QGeoPositionInfoSource-setBackendProperty-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.setPreferredPositioningMethods
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod`
        :description: QtPositioning/QGeoPositionInfoSource-setPreferredPositioningMethods-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.setUpdateInterval
        :args:
            int
        :description: QtPositioning/QGeoPositionInfoSource-setUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.sourceName
        :returns:
            str
        :description: QtPositioning/QGeoPositionInfoSource-sourceName-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.startUpdates
        :description: QtPositioning/QGeoPositionInfoSource-startUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.stopUpdates
        :description: QtPositioning/QGeoPositionInfoSource-stopUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.supportedPositioningMethods
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod`
        :description: QtPositioning/QGeoPositionInfoSource-supportedPositioningMethods-f.rst

    .. sip:method:: PyQt6.QtPositioning.QGeoPositionInfoSource.updateInterval
        :returns:
            int
        :description: QtPositioning/QGeoPositionInfoSource-updateInterval-f.rst

    .. sip:signal:: PyQt6.QtPositioning.QGeoPositionInfoSource.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.Error`
        :description: QtPositioning/QGeoPositionInfoSource-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtPositioning.QGeoPositionInfoSource.positionUpdated
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfo`
        :description: QtPositioning/QGeoPositionInfoSource-positionUpdated-s.rst

    .. sip:signal:: PyQt6.QtPositioning.QGeoPositionInfoSource.supportedPositioningMethodsChanged
        :description: QtPositioning/QGeoPositionInfoSource-supportedPositioningMethodsChanged-s.rst
