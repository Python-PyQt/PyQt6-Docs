.. sip:method-description::
    :status: todo
    :pysig: 7ba96d02f3b1cc9734d15f9edd31e62b
    :realsig: (const QByteArray&,QWebEngineUrlSchemeHandler*)
    :digest: 5b82d850b749f539b1a300ec14edf111

Registers a handler *handler* for custom URL scheme *scheme* in the profile.

It is necessary to first register the scheme with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme.registerScheme` at application startup.
