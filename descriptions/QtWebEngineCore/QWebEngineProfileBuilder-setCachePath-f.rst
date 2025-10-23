.. sip:method-description::
    :status: todo
    :pysig: 07496f9b2de31c702caaa764ee49ee36
    :realsig: (const QString&)
    :digest: 32929b6f33315ec444d21a1340afc61c

Sets the path used for the cache to *path*.

By default, this is below StandardPaths::CacheLocation in a QtWebengine/StorageName specific subdirectory.

**Note:** Use :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`\ (\ :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation`) to obtain the :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation` path.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.cachePath`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`.
