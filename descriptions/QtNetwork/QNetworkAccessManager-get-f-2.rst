.. sip:method-description::
    :status: todo
    :pysig: 02a4a19a09694190afaa60e9b587eb69
    :realsig: (const QNetworkRequest&, QIODevice*)
    :digest: 8f994145f10aa3ee4e8992322c7542b6

**Note:** A GET request with a message body is not cached.

**Note:** If the request is redirected, the message body will be kept only if the status code is 308.
