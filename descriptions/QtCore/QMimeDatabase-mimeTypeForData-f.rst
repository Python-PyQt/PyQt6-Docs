.. sip:method-description::
    :status: todo
    :pysig: 05da48b5862c5bd3b0077468cdc5b214
    :realsig: (const QByteArray&) const
    :digest: 3fda86afa96a5857b71a38430c948785

Returns a MIME type for *data*.

A valid MIME type is always returned. If *data* doesn't match any known MIME type data, the default MIME type (application/octet-stream) is returned.
