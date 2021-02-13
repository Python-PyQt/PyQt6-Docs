.. sip:method-description::
    :status: todo
    :pysig: 8dbfd5b13b65fb5c7422facba343cf8d
    :realsig: (const QUrl&) const
    :digest: 8fda0cf249072ec6e3b87b0a7a90cfca

Returns a MIME type for *url*.

If the URL is a local file, this calls :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForFile`.

Otherwise the matching is done based on the file name only, except for schemes where file names don't mean much, like HTTP. This method always returns the default mimetype for HTTP URLs, use :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` to handle HTTP URLs properly.

A valid MIME type is always returned. If *url* doesn't match any known MIME type data, the default MIME type (application/octet-stream) is returned.
