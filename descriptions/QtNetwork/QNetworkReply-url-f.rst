.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: () const
    :digest: 9568e5a7c48b7b3b9ccbb04dbc68280f

Returns the URL of the content downloaded or uploaded. Note that the URL may be different from that of the original request. If redirections were enabled in the request, then this function returns the current url that the network API is accessing, i.e the url of the resource the request got redirected to.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.request`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.setUrl`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.url`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.redirected`.
