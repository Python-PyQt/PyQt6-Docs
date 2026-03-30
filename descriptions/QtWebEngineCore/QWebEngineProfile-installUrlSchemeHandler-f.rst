.. sip:method-description::
    :status: todo
    :pysig: a125f9df9c7a35d0695334b526dd4108
    :realsig: (const QByteArray&, QWebEngineUrlSchemeHandler*)
    :digest: 5b82d850b749f539b1a300ec14edf111

Registers a handler *handler* for custom URL scheme *scheme* in the profile.

It is necessary to first register the scheme with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme.registerScheme` at application startup.
