.. sip:signal-description::
    :status: todo
    :pysig: 6a25758f6fea2dc809dfe3de6269fd1c
    :realsig: (const QRemoteObjectSourceLocation&)
    :digest: bb85e27e5e8dde5213e3990a2032bcab

This signal is emitted whenever a new source location is added to the registry.

*entry* is a QRemoteObjectSourceLocation, a typedef for QPair<QString, QRemoteObjectSourceLocationInfo>.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry.remoteObjectRemoved`.
