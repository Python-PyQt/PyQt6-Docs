.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: a34a5c49c6706b73ad6a9e08da501ce9

Sets a custom request method. Will set the :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.httpRequestMethod` to QOAuth1Signature::HttpRequestMethod::Custom and store the *verb* to use it for the generation of the signature.

**Note:** Using this method is required when working with custom verbs. Setting only the request method will fail, as the signure needs to know the actual verb.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.customMethodString`, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.setHttpRequestMethod`, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.HttpRequestMethod`.
