.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 8732c89f06b535df23112ee6b5c70a58

Returns the bearer token that has been set.

The bearer token, if present, is used to set the ``Authorization: Bearer my_token`` header for requests. This is a common authorization convention and is provided as an additional convenience.

The means to acquire the bearer token vary. Standard methods include ``OAuth2`` and the service provider's website/dashboard. It is expected that the bearer token changes over time. For example, when updated with a refresh token, always setting the new token again ensures that subsequent requests have the latest, valid token.

The presence of the bearer token does not impact the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.commonHeaders` listing. If the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.commonHeaders` also lists ``Authorization`` header, it will be overwritten.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.setBearerToken`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.commonHeaders`.
