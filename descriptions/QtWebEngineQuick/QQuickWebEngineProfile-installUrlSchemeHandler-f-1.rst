.. sip:method-description::
    :status: todo
    :pysig: ab2712adcadd80ad58dccd37b2696ed2
    :realsig: (const QByteArray&, QWebEngineUrlSchemeHandler*)
    :digest: 5b82d850b749f539b1a300ec14edf111

Registers a handler *handler* for custom URL scheme *scheme* in the profile.

It is necessary to first register the scheme with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme.registerScheme` at application startup.
