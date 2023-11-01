.. sip:method-description::
    :status: todo
    :pysig: 81f2111b4625ede46bf4ee148b778e84
    :realsig: (const QNetworkRequest&, const QByteArray&, QIODevice*)
    :digest: 66bc86c7efd3dcf9d997474422509ef1

Sends a custom request to the server identified by the URL of *request*.

It is the user's responsibility to send a *verb* to the server that is valid according to the HTTP specification.

This method provides means to send verbs other than the common ones provided via :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.get` or :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post` etc., for instance sending an HTTP OPTIONS command.

If *data* is not empty, the contents of the *data* device will be uploaded to the server; in that case, data must be open for reading and must remain valid until the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.finished` signal is emitted for this reply.

**Note:** This feature is currently available for HTTP(S) only.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.get`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.deleteResource`.
