.. sip:method-description::
    :status: todo
    :pysig: e09c616a1204f304b5e7c91edc831e36
    :realsig: () const
    :digest: ca72f66ea65e62e5f17b18221f36de81

Returns the list of all available MIME types.

This can be useful for showing all MIME types to the user, for instance in a MIME type editor. Do not use unless really necessary in other cases though, prefer using the :sip:ref:`~PyQt6.QtCore.QMimeDatabase.mimeTypeForData` methods for performance reasons.
