.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: df348c9095efe6964756fb09e568c755

Marks the certificate error for delayed handling.

This function should be called when there is a need to postpone the decision whether to accept a certificate, for example, while waiting for user input. When called, the function pauses the URL request until :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCertificateError.acceptCertificate` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCertificateError.rejectCertificate` is called.

**Note:** It is only possible to defer overridable certificate errors.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCertificateError.isOverridable`.
