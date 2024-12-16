.. sip:method-description::
    :status: todo
    :pysig: 6e42c3c4ca20d6b3283cb327eae41bba
    :realsig: () const
    :digest: fd3fb4d356dcbd6cac24c89314bbca1d

Returns a QList of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` objects, each one representing a single permission currently present in the permissions store. The returned list contains all previously granted/denied permissions for this profile, provided they are of a *persistent* type.

**Note:** When persistentPermissionPolicy() is set to ``AskEveryTime``, this will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.queryPermission`, :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.listPermissionsForOrigin`, :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.listPermissionsForPermissionType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isPersistent`.
