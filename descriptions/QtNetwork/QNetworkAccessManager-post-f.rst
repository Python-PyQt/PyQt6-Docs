.. sip:method-description::
    :status: todo
    :pysig: 02a4a19a09694190afaa60e9b587eb69
    :realsig: (const QNetworkRequest&,QIODevice*)
    :digest: 38dff721b5c182fdba6861e809ce9628

Sends an HTTP POST request to the destination specified by *request* and returns a new :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` object opened for reading that will contain the reply sent by the server. The contents of the *data* device will be uploaded to the server.

*data* must be open for reading and must remain valid until the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.finished` signal is emitted for this reply.

**Note:** Sending a POST request on protocols other than HTTP and HTTPS is undefined and will probably fail.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.get`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.deleteResource`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.sendCustomRequest`.
