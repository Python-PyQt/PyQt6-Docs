.. sip:method-description::
    :status: todo
    :pysig: 2ca3a2a1f2f0c5925ad77af7f0d7f2a1
    :realsig: (const QFileInfo&,QMimeDatabase::MatchMode) const
    :digest: 03cbd9d5688749aba8f375b92c8e2c74

Returns a MIME type for *fileInfo*.

A valid MIME type is always returned.

The default matching algorithm looks at both the file name and the file contents, if necessary. The file extension has priority over the contents, but the contents will be used if the file extension is unknown, or matches multiple MIME types. If *fileInfo* is a Unix symbolic link, the file that it refers to will be used instead. If the file doesn't match any known pattern or data, the default MIME type (application/octet-stream) is returned.

When *mode* is set to :sip:ref:`~PyQt6.QtCore.QMimeDatabase.MatchMode.MatchExtension`, only the file name is used, not the file contents. The file doesn't even have to exist. If the file name doesn't match any known pattern, the default MIME type (application/octet-stream) is returned. If multiple MIME types match this file, the first one (alphabetically) is returned.

When *mode* is set to :sip:ref:`~PyQt6.QtCore.QMimeDatabase.MatchMode.MatchContent`, and the file is readable, only the file contents are used to determine the MIME type. This is equivalent to calling :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForData` with a :sip:ref:`~PyQt6.QtCore.QFile` as input device.

*fileInfo* may refer to an absolute or relative path.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeType.isDefault`, :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForData`.
