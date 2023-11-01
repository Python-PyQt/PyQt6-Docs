.. sip:method-description::
    :status: todo
    :pysig: 7d74642492c1254c6ab51fbfe503f7bc
    :realsig: (const QString&, QObject*)
    :digest: 71e313c99cc634f43a19696151f65deb

Constructs a new profile with the storage name *storageName* and parent *parent*.

The storage name must be unique.

A disk-based :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` should be destroyed on or before application exit, otherwise the cache and persistent data may not be fully flushed to disk.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.storageName`.
