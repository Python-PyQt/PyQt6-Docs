.. sip:method-description::
    :status: todo
    :pysig: a77d86d9c24369e8ef1677ae2c6397bc
    :realsig: (const QUrl&) const
    :digest: 44511c4945fbced10218817f455add7e

Returns a QList of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` objects, each one representing a single permission currently present in the permissions store. The returned list contains all previously granted/denied permissions associated with a specific *securityOrigin* for this profile, provided they are of a *persistent* type.

**Note:** Since permissions are granted on a per-origin basis, the provided *securityOrigin* will be stripped to its origin form, and the returned list will contain all permissions for the origin. Thus, passing https://www.example.com/some/page.html is the same as passing just https://www.example.com/.

**Note:** When persistentPermissionPolicy() is set to ``AskEveryTime``, this will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.queryPermission`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isPersistent`.
