.. sip:method-description::
    :status: todo
    :pysig: e77dd7b9332b431b51a8eeeeee7021f7
    :realsig: (const QHttpHeaders&)
    :digest: 8543e9933ea7b19bf722ea9f6c7fc156

Sets *newHeaders* as headers in this network reply, overriding any previously set headers.

If some headers correspond to the known headers, they will be parsed and the corresponding parsed form will also be set.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.headers`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`.
