.. sip:method-description::
    :status: todo
    :pysig: e77dd7b9332b431b51a8eeeeee7021f7
    :realsig: (const QHttpHeaders&)
    :digest: 550beb7d2c7011f710b89675e90aabcd

Sets *headers* that are common to all requests.

These headers are added to individual requests' headers. This is a convenience mechanism for setting headers that repeat across requests.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.commonHeaders`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.clearCommonHeaders`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.createRequest`.
