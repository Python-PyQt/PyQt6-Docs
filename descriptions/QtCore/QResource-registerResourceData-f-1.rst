.. sip:method-description::
    :status: todo
    :pysig: 52b86cf692540267ce4222864fb2d05a
    :realname: QResource::registerResource
    :realsig: (const uchar*, const QString&)
    :digest: aa11ce469839a48eb6fc15842989fc72

Registers the resource with the given *rccData* at the location in the resource tree specified by *mapRoot*, and returns ``true`` if the file is successfully opened; otherwise returns ``false``.

**Warning:** The data must remain valid throughout the life of any :sip:ref:`~PyQt6.QtCore.QFile` that may reference the resource data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QResource.unregisterResource`.
