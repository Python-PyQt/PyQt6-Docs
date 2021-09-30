.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: f9c84ee0eaa77215d635c1fe651ca642

Returns the path used for caches.

By default, this is below StandardPaths::CacheLocation in a QtWebengine/StorageName specific subdirectory.

**Note:** Use :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`\ (\ :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation`) to obtain the :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation` path.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setCachePath`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.storageName`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`.
