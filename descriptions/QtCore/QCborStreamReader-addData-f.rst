.. sip:method-description::
    :status: todo
    :pysig: c70916e782d9742b90f37ccdedc4f900
    :realsig: (const QByteArray&)
    :digest: 65d8a0b8551f12c9e22c01082962e6bd

Adds *data* to the CBOR stream and reparses the current element. This function is useful if the end of the data was previously reached while processing the stream, but now more data is available.
