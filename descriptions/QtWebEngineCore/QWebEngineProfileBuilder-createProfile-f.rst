.. sip:method-description::
    :status: todo
    :pysig: bcb53e98b57557d937e3776fcfece911
    :realsig: (const QString&, QObject*) const
    :digest: 21c2e5bdc578636ffadcf1a6fcf58855

Constructs a profile with the storage name *storageName* and parent *parent*.

The storage name is used to give each disk-based profile, a separate subdirectory for persistent data and cache. The storage location must be unique during application life time. It is up to the user to prevent the creation of profiles with same storage's location, which can lead to corrupted browser cache.

A disk-based :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` should be destroyed before the application exit, otherwise the cache and persistent data may not be fully flushed to disk.

**Note:** When creating a disk-based profile, if the data path is already in use by another profile, the function will return a null pointer.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.storageName`.
