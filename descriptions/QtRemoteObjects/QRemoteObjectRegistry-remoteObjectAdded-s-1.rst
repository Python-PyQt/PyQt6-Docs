.. sip:signal-description::
    :status: todo
    :pysig: 6fc8f27443214f11529d394c2175d170
    :realsig: (const QRemoteObjectSourceLocation&)
    :digest: 2acb680e9f01944846b71d14f30c0120

This signal is emitted whenever a new source location is added to the registry.

*entry* is a QRemoteObjectSourceLocation, a typedef for QPair<QString, :sip:ref:`~PyQt6.QtCore.QUrl`>.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry.remoteObjectRemoved`.
