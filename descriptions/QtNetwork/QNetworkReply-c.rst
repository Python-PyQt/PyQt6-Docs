.. sip:class-description::
    :status: todo
    :brief: Contains the data and headers for a request sent with QNetworkAccessManager
    :digest: 8c0592f1d7b9b2c2fd20118bb509a48d

The :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` class contains the data and headers for a request sent with :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.

The :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` class contains the data and meta data related to a request posted with :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`. Like :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`, it contains a URL and headers (both in parsed and raw form), some information about the reply's state and the contents of the reply itself.

:sip:ref:`~PyQt6.QtNetwork.QNetworkReply` is a sequential-access :sip:ref:`~PyQt6.QtCore.QIODevice`, which means that once data is read from the object, it no longer kept by the device. It is therefore the application's responsibility to keep this data if it needs to. Whenever more data is received from the network and processed, the readyRead() signal is emitted.

The :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.downloadProgress` signal is also emitted when data is received, but the number of bytes contained in it may not represent the actual bytes received, if any transformation is done to the contents (for example, decompressing and removing the protocol overhead).

Even though :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` is a :sip:ref:`~PyQt6.QtCore.QIODevice` connected to the contents of the reply, it also emits the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.uploadProgress` signal, which indicates the progress of the upload for operations that have such content.

**Note:** Do not delete the object in the slot connected to the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.errorOccurred` or :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.finished` signal. Use deleteLater().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.
