.. sip:method-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (int,const QByteArray&)
    :digest: a16d1db2ed1d01ae96938b6dc4752269

This is an overloaded function.

Updates a subset of the index buffer. *offset* specifies the offset in bytes, *data* specifies the size and the data.

This function will not resize the buffer. If ``offset + data.size()`` is greater than the current size of the buffer, the overshooting data will be ignored.

**Note:** The partial update functions for vertex and index data do not offer any guarantee on how such changes are implemented internally. Depending on the underlying implementation, even partial changes may lead to updating the entire graphics resource.
