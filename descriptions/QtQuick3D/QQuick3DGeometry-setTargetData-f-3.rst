.. sip:method-description::
    :status: todo
    :pysig: 7235a47c1a42414dac96dde9c65d8778
    :realsig: (int, const QByteArray&)
    :digest: c6d5972b8982640f6104667c2395581d

Updates a subset of the morph target buffer. *offset* specifies the offset in bytes, *data* specifies the size and the data.

This function will not resize the buffer. If ``offset + data.size()`` is greater than the current size of the buffer, the overshooting data will be ignored.

**Note:** The partial update functions for vertex, index and morph target data do not offer any guarantee on how such changes are implemented internally. Depending on the underlying implementation, even partial changes may lead to updating the entire graphics resource.
