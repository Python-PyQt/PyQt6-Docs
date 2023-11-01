.. sip:signal-description::
    :status: todo
    :pysig: 6a25758f6fea2dc809dfe3de6269fd1c
    :realsig: (const QRemoteObjectSourceLocation&)
    :digest: 2acb680e9f01944846b71d14f30c0120

This signal is emitted whenever a new source location is added to the registry.

*entry* is a QRemoteObjectSourceLocation, a typedef for QPair<QString, :sip:ref:`~PyQt6.QtCore.QUrl`>.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry.remoteObjectRemoved`.
