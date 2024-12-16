.. sip:method-description::
    :status: todo
    :pysig: 6e42c3c4ca20d6b3283cb327eae41bba
    :realsig: () const
    :digest: e3e6f292f4bbd1d12174d1a2e99db3aa

Returns a QList of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` objects, each one representing a single permission currently present in the permissions store. The returned list contains all previously granted/denied permissions for this profile, provided they are of a *persistent* type.

**Note:** When persistentPermissionPolicy() is set to ``AskEveryTime``, this will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.queryPermission`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isPersistent`.
