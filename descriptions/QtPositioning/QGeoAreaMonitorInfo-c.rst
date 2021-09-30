.. sip:class-description::
    :status: todo
    :brief: Describes the parameters of an area or region to be monitored for proximity
    :digest: 6350d2615b608ca68ae3d8a43b483d38

The :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` class describes the parameters of an area or region to be monitored for proximity.

The purpose of area monitoring is to inform a user when he/she comes close to an area of interest. In general such an area is described by a :sip:ref:`~PyQt6.QtPositioning.QGeoCircle`. The circle's center represents the place of interest and the area around it identifies the geographical region within which notifications are sent.

A :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` object is valid if it has a non-empty name and a valid :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo.area`. Such objects must be registered with a :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource` to start and stop the monitoring process. Note that extensive monitoring can be very resource consuming because the positioning engine must remain active and has to match the current position with each :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` instance.

To further reduce the burden on the system there are optional attributes which can set. Each monitored area can have an expiry date which automatically removes the to-be-monitored area from the monitoring source once the expiry date has been reached. Another option is to adjust the persistence of a monitored area. A :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` that :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo.isPersistent` will remain active beyond the current applications lifetime. If an area is entered while the monitoring application is not running the application will be started. Note that this feature is not available on all platforms. Its availability can be checked via :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.supportedAreaMonitorFeatures`.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource`.
