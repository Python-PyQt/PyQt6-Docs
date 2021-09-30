:orphan:

.. sip:class:: PyQt6.QtPositioning.QNmeaPositionInfoSource
    :inherits: :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource`
    :description: QtPositioning/QNmeaPositionInfoSource-c.rst

    .. sip:enum:: PyQt6.QtPositioning.QNmeaPositionInfoSource.UpdateMode
        :description: QtPositioning/QNmeaPositionInfoSource-UpdateMode-e.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QNmeaPositionInfoSource.UpdateMode.RealTimeMode
            :description: QtPositioning/QNmeaPositionInfoSource-UpdateMode-RealTimeMode-v.rst

        .. sip:enum-member:: PyQt6.QtPositioning.QNmeaPositionInfoSource.UpdateMode.SimulationMode
            :description: QtPositioning/QNmeaPositionInfoSource-UpdateMode-SimulationMode-v.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.__init__
        :args:
            :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.UpdateMode`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtPositioning/QNmeaPositionInfoSource-__init__-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtPositioning/QNmeaPositionInfoSource-device-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.error
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.Error`
        :description: QtPositioning/QNmeaPositionInfoSource-error-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.lastKnownPosition
        :args:
            fromSatellitePositioningMethodsOnly: bool = False
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfo`
        :description: QtPositioning/QNmeaPositionInfoSource-lastKnownPosition-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.minimumUpdateInterval
        :returns:
            int
        :description: QtPositioning/QNmeaPositionInfoSource-minimumUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.parsePosInfoFromNmeaData
        :args:
            str
            int
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfo`
        :returns:
            bool
            bool
        :description: QtPositioning/QNmeaPositionInfoSource-parsePosInfoFromNmeaData-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.requestUpdate
        :args:
            timeout: int = 0
        :description: QtPositioning/QNmeaPositionInfoSource-requestUpdate-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtPositioning/QNmeaPositionInfoSource-setDevice-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.setUpdateInterval
        :args:
            int
        :description: QtPositioning/QNmeaPositionInfoSource-setUpdateInterval-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.setUserEquivalentRangeError
        :args:
            float
        :description: QtPositioning/QNmeaPositionInfoSource-setUserEquivalentRangeError-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.startUpdates
        :description: QtPositioning/QNmeaPositionInfoSource-startUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.stopUpdates
        :description: QtPositioning/QNmeaPositionInfoSource-stopUpdates-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.supportedPositioningMethods
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.PositioningMethod`
        :description: QtPositioning/QNmeaPositionInfoSource-supportedPositioningMethods-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.updateMode
        :returns:
            :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.UpdateMode`
        :description: QtPositioning/QNmeaPositionInfoSource-updateMode-f.rst

    .. sip:method:: PyQt6.QtPositioning.QNmeaPositionInfoSource.userEquivalentRangeError
        :returns:
            float
        :description: QtPositioning/QNmeaPositionInfoSource-userEquivalentRangeError-f.rst
