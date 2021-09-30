.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: d13da47a62dce3d3816e2692b1791183

Returns the expiry date.

After an active :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` has expired the region is no longer monitored and the :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` object is removed from the list of :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.activeMonitors`.

If the expiry :sip:ref:`~PyQt6.QtCore.QDateTime` is invalid the :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` object is treated as not having an expiry date. This implies an indefinite monitoring period if the object is persistent or until the current application closes if the object is non-persistent.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo.setExpiration`, :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.activeMonitors`.
