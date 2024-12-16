.. sip:method-description::
    :status: todo
    :pysig: 79e856eb1882f82f7b62a7a43e5c78f0
    :realsig: () const
    :digest: ca72f66ea65e62e5f17b18221f36de81

Returns the list of all available MIME types.

This can be useful for showing all MIME types to the user, for instance in a MIME type editor. Do not use unless really necessary in other cases though, prefer using the :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForData` methods for performance reasons.
