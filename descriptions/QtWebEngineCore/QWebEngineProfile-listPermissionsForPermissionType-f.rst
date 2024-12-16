.. sip:method-description::
    :status: todo
    :pysig: 2dd8dd74c5caf426943faa7294338928
    :realsig: (QWebEnginePermission::PermissionType) const
    :digest: 9fd80c659f3909121e6663bff87b2981

Returns a QList of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` objects, each one representing a single permission currently present in the permissions store. The returned list contains all previously granted/denied permissions of the provided *permissionType*. If the permissionType is non-persistent, the list will be empty.

**Note:** When persistentPermissionPolicy() is set to ``AskEveryTime``, this will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.queryPermission`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isPersistent`.
