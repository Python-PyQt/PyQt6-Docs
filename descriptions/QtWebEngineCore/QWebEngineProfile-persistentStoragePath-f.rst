.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 65ad90605bb4b8c3019738db5912d9d2

Returns the path used to store persistent data for the browser and web content.

Persistent data includes persistent cookies, HTML5 local storage, and visited links.

By default, this is below QStandardPaths::DataLocation in a QtWebengine/StorageName specific subdirectory.

**Note:** Use :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`\ (QStandardPaths::DataLocation) to obtain the QStandardPaths::DataLocation path.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentStoragePath`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.storageName`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`.
