.. sip:signal-description::
    :status: todo
    :pysig: 1d77387838b9ad792730da8d30dbcc21
    :realsig: (const QWebEngineCertificateError&)
    :digest: 63f654db929e23ac83f0185a9543cae4

This signal is emitted when an invalid certificate error is raised while loading a given request.

The *certificateError* parameter contains information about the certificate and details of the error, it also provides the way to ignore the error and complete the request or stop loading the request.

.. seealso:: `QWebEngineCertificateError <https://doc.qt.io/qt-6/qtwebengine-changes-qt6.html#qwebenginecertificateerror>`_.
