.. sip:method-description::
    :status: todo
    :pysig: 2bd872881014749972c546eda6527fe5
    :realsig: (const QUrl&,QWebEnginePage::Feature,QWebEnginePage::PermissionPolicy)
    :digest: 27e311b993ea0ff3c7916da7a1dbf89c

Use :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`'s :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.grant`\ (), :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.deny`\ (), and :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.reset`\ () functions instead.

Sets the permission for the web site identified by *securityOrigin* to use *feature* to *policy*.

**Note:** This method is primarily for calling after a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.featurePermissionRequested` signal has been emitted to trigger the feature permission response. It can also be called before a request has been emitted, but will only set a granted permission for passive checks, mainly for Notification APIs that can check if permission has already been granted before explicitly requesting it.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.featurePermissionRequested`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.featurePermissionRequestCanceled`.
