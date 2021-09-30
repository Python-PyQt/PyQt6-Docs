.. sip:signal-description::
    :status: todo
    :pysig: 6a25758f6fea2dc809dfe3de6269fd1c
    :realsig: (const QRemoteObjectSourceLocation&)
    :digest: a003b2261a724a2d1f93146349d8995b

This signal is emitted whenever a new source location is added to the registry.

*entry* is a QRemoteObjectSourceLocation, a typedef for QPair<QString, :sip:ref:`~PyQt6.QtCore.QUrl`>.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry.remoteObjectRemoved`.
