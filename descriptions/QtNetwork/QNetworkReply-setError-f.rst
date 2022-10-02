.. sip:method-description::
    :status: todo
    :pysig: 5123e44c56409efdcf1a29f1d87da896
    :realsig: (QNetworkReply::NetworkError,const QString&)
    :digest: fc1ff96170dd74d5df052933e211b16b

Sets the error condition to be *errorCode*. The human-readable message is set with *errorString*.

Calling setError() does not emit the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.errorOccurred`\ (\ :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.NetworkError`) signal.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.error`, errorString().
