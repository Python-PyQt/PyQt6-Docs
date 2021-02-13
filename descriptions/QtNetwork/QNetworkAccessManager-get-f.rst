.. sip:method-description::
    :status: todo
    :pysig: b567d01f49ed6b4a87887827b8091a7a
    :realsig: (const QNetworkRequest&)
    :digest: ac664299a6e98eea9a5592459eed008a

Posts a request to obtain the contents of the target *request* and returns a new :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` object opened for reading which emits the :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` signal whenever new data arrives.

The contents as well as associated headers will be downloaded.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.deleteResource`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.sendCustomRequest`.
