.. sip:method-description::
    :status: todo
    :pysig: 7d74642492c1254c6ab51fbfe503f7bc
    :realsig: (const QString&, QObject*)
    :digest: 0a351fdba743ada15ab3a2aa12e1ab61

Constructs a new profile with the storage name *storageName* and parent *parent*.

The storage name must be unique.

A disk-based :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile` should be destroyed on or before application exit, otherwise the cache and persistent data may not be fully flushed to disk.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.storageName`.
