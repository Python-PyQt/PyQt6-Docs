.. sip:attribute-description::
    :status: todo
    :digest: 9eea3a1b947576f8f55c7a201099c6cf

This variable holds The backend property name for data read rate in the :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode.SimulationMode`. The value for this property is the integer number representing the amount of milliseconds between the subsequent reads. Use this parameter in the :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.setBackendProperty` and :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.backendProperty` methods..

**Note:** This property is different from the interval that can be set via :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.setUpdateInterval`. The value set via :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.setUpdateInterval` denotes an interval for the user notification, while this parameter specifies the internal frequency of reading the data from source file. It means that one can have multiple (or none) reads during the updateInterval() period.
