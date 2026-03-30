.. sip:method-description::
    :status: todo
    :pysig: 83852cea65251de4eddd3e1a36b61cca
    :realsig: (const QString&, const QString&)
    :digest: ea34ba7e7b58a75eaba43eba5dbd1a1a

Sets *token* and *tokenSecret* as the pair of QString used to identify and sign authenticated requests to the web server. Once the client receives and stores the token credentials, it can proceed to access protected resources on behalf of the resource owner by making authenticated requests using the client credentials together with the token credentials received.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1.tokenCredentials`.
