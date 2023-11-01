.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 26fdf475fd097cc37f130b5d01bdb204

Sets a custom request method. Will set the :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.httpRequestMethod` to :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Custom` and store the *verb* to use it for the generation of the signature.

**Note:** Using this method is required when working with custom verbs. Setting only the request method will fail, as the signure needs to know the actual verb.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.customMethodString`, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.setHttpRequestMethod`, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.HttpRequestMethod`.
