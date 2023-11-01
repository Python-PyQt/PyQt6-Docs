.. sip:method-description::
    :status: todo
    :pysig: 52b86cf692540267ce4222864fb2d05a
    :realname: QResource::unregisterResource
    :realsig: (const uchar*, const QString&)
    :digest: 2d496f21ed385f700a2c327b7ce2e6d3

Unregisters the resource with the given *rccData* at the location in the resource tree specified by *mapRoot*, and returns ``true`` if the resource is successfully unloaded and no references exist into the resource; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QResource.registerResource`.
