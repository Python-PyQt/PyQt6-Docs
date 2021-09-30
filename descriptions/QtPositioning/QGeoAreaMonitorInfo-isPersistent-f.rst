.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: fb374701868cdd0a58ee28c64f989f2a

Returns true if the :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` is persistent. The default value for this property is false.

A non-persistent :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` will be removed by the system once the application owning the monitor object stops. Persistent objects remain active and can be retrieved once the application restarts.

If the system triggers an event associated to a persistent :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` the relevant application will be re-started and the appropriate signal emitted.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo.setPersistent`.
