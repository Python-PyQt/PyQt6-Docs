.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: 1af7d646914221c135d2b88eae69316a

If :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.requestUpdate` was called, this error indicates that the current position could not be retrieved within the specified timeout. If :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.startUpdates` was called, this error indicates that this :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` subclass determined that it will not be able to provide further regular updates. In the latter case the error would not be emitted again until after the regular updates resume.
