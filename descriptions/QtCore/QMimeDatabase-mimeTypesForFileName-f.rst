.. sip:method-description::
    :status: todo
    :pysig: 8f2e75540d627daf5c0bc58ee461cbfc
    :realsig: (const QString&) const
    :digest: c94313536ae8188a61df1579b0a3885d

Returns the MIME types for the file name *fileName*.

If the file name doesn't match any known pattern, an empty list is returned. If multiple MIME types match this file, they are all returned.

This function does not try to open the file. To also use the content when determining the MIME type, use :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForFile` or :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForFileNameAndData` instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForFile`.
