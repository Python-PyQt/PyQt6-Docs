.. sip:method-description::
    :status: todo
    :pysig: 6c9016731f9fc63f5ba5550ee294db77
    :realsig: (const QNetworkRequest&, const QByteArray&)
    :digest: 8f994145f10aa3ee4e8992322c7542b6

**Note:** A GET request with a message body is not cached.

**Note:** If the request is redirected, the message body will be kept only if the status code is 308.
