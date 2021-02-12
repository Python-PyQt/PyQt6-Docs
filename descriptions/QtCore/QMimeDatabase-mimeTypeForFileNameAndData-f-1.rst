.. sip:method-description::
    :status: todo
    :pysig: 1484adf5d74c6d0f39a7bc6de7fd5342
    :realsig: (const QString&,const QByteArray&) const
    :digest: 92d90897971552cdf4a150c961f729fd

Returns a MIME type for the given *fileName* and device *data*.

This overload can be useful when the file is remote, and we started to download some of its data. This allows to do full MIME type matching for remote files as well.

A valid MIME type is always returned. If *data* doesn't match any known MIME type data, the default MIME type (application/octet-stream) is returned.

This method looks at both the file name and the file contents, if necessary. The file extension has priority over the contents, but the contents will be used if the file extension is unknown, or matches multiple MIME types.
