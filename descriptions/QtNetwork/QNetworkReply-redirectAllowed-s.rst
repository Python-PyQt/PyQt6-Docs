.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5de73cf52941c51866bce966bb929e3c

When client code handling the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.redirected` signal has verified the new URL, it emits this signal to allow the redirect to go ahead. This protocol applies to network requests whose redirects policy is set to :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy.UserVerifiedRedirectPolicy`

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy.UserVerifiedRedirectPolicy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setRedirectPolicy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.Attribute.RedirectPolicyAttribute`.
