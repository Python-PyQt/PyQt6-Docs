.. sip:method-description::
    :status: todo
    :pysig: 93a40e16eb9c57e19d53172cc8afd089
    :realsig: (QNetworkAccessManager*)
    :digest: 66aaca787320da699fd9cfe7ac3e5835

Sets the network manager to *networkAccessManager*. :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth` does not take ownership of *networkAccessManager*. If no custom network access manager is set, an internal network access manager is used. This network access manager will be used to make the request to the authentication server and the authenticated request to the web service.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.networkAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.
