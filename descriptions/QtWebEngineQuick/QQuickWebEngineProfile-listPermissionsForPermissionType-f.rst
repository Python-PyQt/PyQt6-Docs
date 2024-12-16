.. sip:method-description::
    :status: todo
    :pysig: 2dd8dd74c5caf426943faa7294338928
    :realsig: (QWebEnginePermission::PermissionType) const
    :digest: 9734a598c865d5d587edb677be2d8cfa

Returns a QList of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` objects, each one representing a single permission currently present in the permissions store. The returned list contains all previously granted/denied permissions of the provided *permissionType*. If the permissionType is non-persistent, the list will be empty.

**Note:** When persistentPermissionPolicy() is set to ``AskEveryTime``, this will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.queryPermission`, :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.listAllPermissions`, :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.listPermissionsForOrigin`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isPersistent`.
