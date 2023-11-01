.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 65d8a0b8551f12c9e22c01082962e6bd

Adds *data* to the CBOR stream and reparses the current element. This function is useful if the end of the data was previously reached while processing the stream, but now more data is available.
