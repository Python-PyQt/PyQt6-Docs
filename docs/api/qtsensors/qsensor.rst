:orphan:

.. sip:class:: PyQt6.QtSensors.QSensor
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtSensors/QSensor-c.rst

    .. sip:enum:: PyQt6.QtSensors.QSensor.AxesOrientationMode
        :description: QtSensors/QSensor-AxesOrientationMode-e.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.AxesOrientationMode.AutomaticOrientation
            :description: QtSensors/QSensor-AxesOrientationMode-AutomaticOrientation-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.AxesOrientationMode.FixedOrientation
            :description: QtSensors/QSensor-AxesOrientationMode-FixedOrientation-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.AxesOrientationMode.UserOrientation
            :description: QtSensors/QSensor-AxesOrientationMode-UserOrientation-v.rst

    .. sip:enum:: PyQt6.QtSensors.QSensor.Feature
        :description: QtSensors/QSensor-Feature-e.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.AccelerationMode
            :description: QtSensors/QSensor-Feature-AccelerationMode-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.AlwaysOn
            :description: QtSensors/QSensor-Feature-AlwaysOn-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.AxesOrientation
            :description: QtSensors/QSensor-Feature-AxesOrientation-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.Buffering
            :description: QtSensors/QSensor-Feature-Buffering-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.FieldOfView
            :description: QtSensors/QSensor-Feature-FieldOfView-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.GeoValues
            :description: QtSensors/QSensor-Feature-GeoValues-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.PressureSensorTemperature
            :description: QtSensors/QSensor-Feature-PressureSensorTemperature-v.rst

        .. sip:enum-member:: PyQt6.QtSensors.QSensor.Feature.SkipDuplicates
            :description: QtSensors/QSensor-Feature-SkipDuplicates-v.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtSensors/QSensor-__init__-f-1.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.addFilter
        :args:
            :sip:ref:`~PyQt6.QtSensors.QSensorFilter`
        :description: QtSensors/QSensor-addFilter-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.availableDataRates
        :returns:
            list[tuple[int, int]]
        :description: QtSensors/QSensor-availableDataRates-f-1.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.axesOrientationMode
        :returns:
            :sip:ref:`~PyQt6.QtSensors.QSensor.AxesOrientationMode`
        :description: QtSensors/QSensor-axesOrientationMode-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.bufferSize
        :returns:
            int
        :description: QtSensors/QSensor-bufferSize-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.connectToBackend
        :returns:
            bool
        :description: QtSensors/QSensor-connectToBackend-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.currentOrientation
        :returns:
            int
        :description: QtSensors/QSensor-currentOrientation-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.dataRate
        :returns:
            int
        :description: QtSensors/QSensor-dataRate-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.defaultSensorForType
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtSensors/QSensor-defaultSensorForType-f-1.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.description
        :returns:
            str
        :description: QtSensors/QSensor-description-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.efficientBufferSize
        :returns:
            int
        :description: QtSensors/QSensor-efficientBufferSize-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.error
        :returns:
            int
        :description: QtSensors/QSensor-error-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.filters
        :returns:
            list[:sip:ref:`~PyQt6.QtSensors.QSensorFilter`]
        :description: QtSensors/QSensor-filters-f-1.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.identifier
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtSensors/QSensor-identifier-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.isActive
        :returns:
            bool
        :description: QtSensors/QSensor-isActive-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.isAlwaysOn
        :returns:
            bool
        :description: QtSensors/QSensor-isAlwaysOn-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.isBusy
        :returns:
            bool
        :description: QtSensors/QSensor-isBusy-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.isConnectedToBackend
        :returns:
            bool
        :description: QtSensors/QSensor-isConnectedToBackend-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.isFeatureSupported
        :args:
            :sip:ref:`~PyQt6.QtSensors.QSensor.Feature`
        :returns:
            bool
        :description: QtSensors/QSensor-isFeatureSupported-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.maxBufferSize
        :returns:
            int
        :description: QtSensors/QSensor-maxBufferSize-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.outputRange
        :returns:
            int
        :description: QtSensors/QSensor-outputRange-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.outputRanges
        :returns:
            list[:sip:ref:`~PyQt6.QtSensors.qoutputrange`]
        :description: QtSensors/QSensor-outputRanges-f-1.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.reading
        :returns:
            :sip:ref:`~PyQt6.QtSensors.QSensorReading`
        :description: QtSensors/QSensor-reading-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.removeFilter
        :args:
            :sip:ref:`~PyQt6.QtSensors.QSensorFilter`
        :description: QtSensors/QSensor-removeFilter-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.sensorsForType
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtSensors/QSensor-sensorsForType-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.sensorTypes
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtSensors/QSensor-sensorTypes-f-1.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setActive
        :args:
            bool
        :description: QtSensors/QSensor-setActive-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setAlwaysOn
        :args:
            bool
        :description: QtSensors/QSensor-setAlwaysOn-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setAxesOrientationMode
        :args:
            :sip:ref:`~PyQt6.QtSensors.QSensor.AxesOrientationMode`
        :description: QtSensors/QSensor-setAxesOrientationMode-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setBufferSize
        :args:
            int
        :description: QtSensors/QSensor-setBufferSize-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setCurrentOrientation
        :args:
            int
        :description: QtSensors/QSensor-setCurrentOrientation-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setDataRate
        :args:
            int
        :description: QtSensors/QSensor-setDataRate-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setEfficientBufferSize
        :args:
            int
        :description: QtSensors/QSensor-setEfficientBufferSize-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setIdentifier
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtSensors/QSensor-setIdentifier-f-1.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setMaxBufferSize
        :args:
            int
        :description: QtSensors/QSensor-setMaxBufferSize-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setOutputRange
        :args:
            int
        :description: QtSensors/QSensor-setOutputRange-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setSkipDuplicates
        :args:
            bool
        :description: QtSensors/QSensor-setSkipDuplicates-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.setUserOrientation
        :args:
            int
        :description: QtSensors/QSensor-setUserOrientation-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.skipDuplicates
        :returns:
            bool
        :description: QtSensors/QSensor-skipDuplicates-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.start
        :returns:
            bool
        :description: QtSensors/QSensor-start-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.stop
        :description: QtSensors/QSensor-stop-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.type
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtSensors/QSensor-type-f.rst

    .. sip:method:: PyQt6.QtSensors.QSensor.userOrientation
        :returns:
            int
        :description: QtSensors/QSensor-userOrientation-f.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.activeChanged
        :description: QtSensors/QSensor-activeChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.alwaysOnChanged
        :description: QtSensors/QSensor-alwaysOnChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.availableSensorsChanged
        :description: QtSensors/QSensor-availableSensorsChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.axesOrientationModeChanged
        :args:
            :sip:ref:`~PyQt6.QtSensors.QSensor.AxesOrientationMode`
        :description: QtSensors/QSensor-axesOrientationModeChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.bufferSizeChanged
        :args:
            int
        :description: QtSensors/QSensor-bufferSizeChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.busyChanged
        :description: QtSensors/QSensor-busyChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.currentOrientationChanged
        :args:
            int
        :description: QtSensors/QSensor-currentOrientationChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.dataRateChanged
        :description: QtSensors/QSensor-dataRateChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.efficientBufferSizeChanged
        :args:
            int
        :description: QtSensors/QSensor-efficientBufferSizeChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.identifierChanged
        :description: QtSensors/QSensor-identifierChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.maxBufferSizeChanged
        :args:
            int
        :description: QtSensors/QSensor-maxBufferSizeChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.readingChanged
        :description: QtSensors/QSensor-readingChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.sensorError
        :args:
            int
        :description: QtSensors/QSensor-sensorError-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.skipDuplicatesChanged
        :args:
            bool
        :description: QtSensors/QSensor-skipDuplicatesChanged-s.rst

    .. sip:signal:: PyQt6.QtSensors.QSensor.userOrientationChanged
        :args:
            int
        :description: QtSensors/QSensor-userOrientationChanged-s.rst
