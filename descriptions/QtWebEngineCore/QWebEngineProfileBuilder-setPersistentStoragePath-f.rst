.. sip:method-description::
    :status: todo
    :pysig: 07496f9b2de31c702caaa764ee49ee36
    :realsig: (const QString&)
    :digest: 2cbf98b4b716dc787441d92ab459dce0

Sets the path used to store persistent data for the browser and web content to *path*. Persistent data includes persistent cookies, HTML5 local storage, and visited links.

By default, this is below QStandardPaths::DataLocation in a QtWebengine/StorageName specific subdirectory.

**Note:** Use :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`\ (QStandardPaths::DataLocation) to obtain the QStandardPaths::DataLocation path.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.persistentStoragePath`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`.
