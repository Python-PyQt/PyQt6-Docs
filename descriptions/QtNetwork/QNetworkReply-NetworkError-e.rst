.. sip:enum-description::
    :status: todo
    :digest: c47378f35e743d27593c88a23636e244

Indicates all possible error conditions found during the processing of the request.

**Note:** When the HTTP protocol returns a redirect no error will be reported. You can check if there is a redirect with the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.Attribute.RedirectionTargetAttribute` attribute.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.error`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.errorOccurred`.
