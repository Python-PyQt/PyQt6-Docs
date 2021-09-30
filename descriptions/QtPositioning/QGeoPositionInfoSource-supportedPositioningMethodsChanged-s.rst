.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 571a603d26c6bc7da9ac10c81efd989a

This signal is emitted when the supported positioning methods changed. The cause for a change could be a user turning Location services on/off or restricting Location services to certain types (e.g. GPS only). Note that changes to the supported positioning methods cannot be detected on all platforms. :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.supportedPositioningMethods` provides an overview of the current platform support.
