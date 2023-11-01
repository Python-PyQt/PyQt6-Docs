.. sip:method-description::
    :status: todo
    :pysig: aef86b61fa008d4ff54fd23aa64fe7ed
    :realsig: (const QByteArray&) const
    :digest: 3fda86afa96a5857b71a38430c948785

Returns a MIME type for *data*.

A valid MIME type is always returned. If *data* doesn't match any known MIME type data, the default MIME type (application/octet-stream) is returned.
