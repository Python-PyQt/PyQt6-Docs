.. sip:method-description::
    :status: todo
    :pysig: 0bd5b2e1d97821094eb31d9a7e0c951c
    :realsig: () const
    :digest: 7f992ef6eacc620f0a357bc88325fe69

Returns query parameters that are added to individual requests' query parameters. The query parameters are added to any potential query parameters provided with the individual :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.createRequest` calls.

Use cases for using repeating query parameters are server dependent, but typical examples include language setting ``?lang=en``, format specification ``?format=json``, API version specification ``?version=1.0`` and API key authentication.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.setQueryParameters`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.clearQueryParameters`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.createRequest`.
