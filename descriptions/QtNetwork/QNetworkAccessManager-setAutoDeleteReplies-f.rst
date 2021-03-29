.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: aca614e5c4593ed991f74a9b6b325078

Enables or disables automatic deletion of :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`.

Setting *shouldAutoDelete* to true is the same as setting the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.Attribute.AutoDeleteReplyOnFinishAttribute` attribute to true on all *future* :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest` passed to this instance of :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` unless the attribute was already explicitly set on the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.autoDeleteReplies`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.Attribute.AutoDeleteReplyOnFinishAttribute`.
