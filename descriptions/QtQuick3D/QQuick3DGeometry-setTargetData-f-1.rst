.. sip:method-description::
    :status: todo
    :pysig: 6506bcc0dc6b9f5bc554559212db4fae
    :realsig: (int, const QByteArray&)
    :digest: bcd9b8ba76c4375992a9e00394a5e1e5

This is an overloaded function.

Updates a subset of the morph target buffer. *offset* specifies the offset in bytes, *data* specifies the size and the data.

This function will not resize the buffer. If ``offset + data.size()`` is greater than the current size of the buffer, the overshooting data will be ignored.

**Note:** The partial update functions for vertex, index and morph target data do not offer any guarantee on how such changes are implemented internally. Depending on the underlying implementation, even partial changes may lead to updating the entire graphics resource.
