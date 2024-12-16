.. sip:class-description::
    :status: todo
    :brief: A QWebEnginePermission is an object used to access and modify the state of a single permission that's been granted or denied to a specific origin URL
    :digest: 12b41bc834197076afbf3d34eb5c08c9

A :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` is an object used to access and modify the state of a single permission that's been granted or denied to a specific origin URL.

The typical usage pattern is as follows:

#. A website requests a specific permission, triggering the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.permissionRequested` signal;

#. The signal handler triggers a prompt asking the user whether they want to grant the permission;

#. When the user has made their decision, the application calls :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.grant` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.deny`;

Alternatively, an application interested in modifying already granted permissions may use :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.listAllPermissions` to get a list of existing permissions associated with a profile, or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.queryPermission` to get a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` object for a specific permission.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.origin` property can be used to query which origin the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` is associated with, while the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.permissionType` property describes the type of the requested permission. A website origin is the combination of its scheme, hostname, and port. Permissions are granted on a per-origin basis; thus, if the web page ``https://www.example.com:12345/some/page.html`` requests a permission, it will be granted to the origin ``https://www.example.com:12345/``.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType` describes all the permission types Qt `WebEngine <https://doc.qt.io/qt-6/qml-qtwebengine-webengine.html>`_ supports. Only some permission types are remembered between browsing sessions; they are *persistent*. Non-persistent permissions query the user every time a website requests them. You can check whether a permission type is persistent at runtime using the static method :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isPersistent`.

Persistent permissions are stored inside the active :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile`, and their lifetime depends on the value of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.persistentPermissionsPolicy`. By default, named profiles store their permissions on disk, whereas off-the-record ones store them in memory (and destroy them when the profile is destroyed). A stored permission will not query the user the next time a website requests it; instead it will be automatically granted or denied, depending on the resolution the user picked initially. To erase a stored permission, call :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.reset` on it.

A non-persistent permission, on the other hand, is only usable until the related :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` performs a navigation to a different URL, or is destroyed.

You can check whether a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission` is in a valid state using its :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isValid` property. For invalid objects, calls to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.grant`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.deny`, or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.reset` will do nothing, while calls to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.state` will always return :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.State.Invalid`.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.permissionRequested`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.queryPermission`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.listAllPermissions`.
