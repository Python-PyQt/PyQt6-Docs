.. sip:method-description::
    :status: todo
    :pysig: 3f1ceb5299540e59eebd90d3a1a8eb39
    :realsig: (const QUrl&, QWebEnginePermission::PermissionType) const
    :digest: 8adca8a3a9f506c667128124d68698c0

Returns a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` object corresponding to a single permission for the provided *securityOrigin* and *permissionType*. The object may be used to query for the current state of the permission, or to change it. It is not required for a permission to already exist; the returned object may also be used to pre-grant a permission if a website is known to use it.

You may use this to pre-grant a permission of a non-persistent type. Doing so will keep the permission in the granted (or denied) state until the next time a website with the associated origin requests it. At that point, the permission's lifetime will be tied to that specific web page's lifetime, and navigating away will invalidate the permission.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.listAllPermissions`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.listPermissionsForOrigin`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.listPermissionsForPermissionType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`.
