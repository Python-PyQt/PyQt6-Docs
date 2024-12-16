.. sip:method-description::
    :status: todo
    :pysig: 3f1ceb5299540e59eebd90d3a1a8eb39
    :realsig: (const QUrl&, QWebEnginePermission::PermissionType) const
    :digest: 97ba9951232897a453182fca19d002fd

Returns a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` object corresponding to a single permission for the provided *securityOrigin* and *permissionType*. The object may be used to query for the current state of the permission, or to change it. It is not required for a permission to already exist; the returned object may also be used to pre-grant a permission if a website is known to use it.

**Note:** This may only be used for persistent permission types. Calling it with a non-persistent *permissionType* will return an invalid object.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.listAllPermissions`, :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.listPermissionsForOrigin`, :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.listPermissionsForPermissionType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`.
