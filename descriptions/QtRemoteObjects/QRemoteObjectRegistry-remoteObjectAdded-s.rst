.. sip:signal-description::
    :status: todo
    :pysig: 57376ba4def0b83f83f076c5427a5cfb
    :realsig: (const QRemoteObjectSourceLocation&)
    :digest: bb85e27e5e8dde5213e3990a2032bcab

This signal is emitted whenever a new source location is added to the registry.

*entry* is a QRemoteObjectSourceLocation, a typedef for QPair<QString, QRemoteObjectSourceLocationInfo>.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry.remoteObjectRemoved`.
