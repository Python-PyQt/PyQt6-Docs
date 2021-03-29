.. sip:method-description::
    :status: todo
    :pysig: 5123e44c56409efdcf1a29f1d87da896
    :realsig: (QNetworkReply::NetworkError,const QString&)
    :digest: 6ebccaaadeb4adc486d47bafcc01cce5

Sets the error condition to be *errorCode*. The human-readable message is set with *errorString*.

Calling  does not emit the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.errorOccurred`\ (\ :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.NetworkError`) signal.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.error`, errorString().
