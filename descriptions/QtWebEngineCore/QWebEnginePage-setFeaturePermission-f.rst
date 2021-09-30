.. sip:method-description::
    :status: todo
    :pysig: 2bd872881014749972c546eda6527fe5
    :realsig: (const QUrl&,QWebEnginePage::Feature,QWebEnginePage::PermissionPolicy)
    :digest: 63c3c34bed3d434cbc4b641555e216ec

Sets the permission for the web site identified by *securityOrigin* to use *feature* to *policy*.

**Note:** This method is primarily for calling after a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.featurePermissionRequested` signal has been emitted to trigger the feature permission response. It can also be called before a request has been emitted, but will only set a granted permission for passive checks, mainly for Notification APIs that can check if permission has already been granted before explicitly requesting it.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.featurePermissionRequested`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.featurePermissionRequestCanceled`.
