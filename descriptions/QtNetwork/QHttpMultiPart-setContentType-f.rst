.. sip:method-description::
    :status: todo
    :pysig: a539199cfbaf096494f6a1dc14f2728d
    :realsig: (QHttpMultiPart::ContentType)
    :digest: 095d8b57348ef8a1ba4b144ee046bb86

Sets the content type to *contentType*. The content type will be used in the HTTP header section when sending the multipart message via :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`. In case you want to use a multipart subtype not contained in :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart.ContentType`, you can add the "Content-Type" header field to the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest` by hand, and then use this request together with the multipart message for posting.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart.ContentType`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`.
