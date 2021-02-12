.. sip:method-description::
    :status: todo
    :pysig: 5509d2cc08994d648b4742605b23fe85
    :realsig: (const QString&,QIODevice*) const
    :digest: 70cc174ce28b6e96f7187aaef5b0ec67

Returns a MIME type for the given *fileName* and *device* data.

This overload can be useful when the file is remote, and we started to download some of its data in a device. This allows to do full MIME type matching for remote files as well.

If the device is not open, it will be opened by this function, and closed after the MIME type detection is completed.

A valid MIME type is always returned. If *device* data doesn't match any known MIME type data, the default MIME type (application/octet-stream) is returned.

This method looks at both the file name and the file contents, if necessary. The file extension has priority over the contents, but the contents will be used if the file extension is unknown, or matches multiple MIME types.
