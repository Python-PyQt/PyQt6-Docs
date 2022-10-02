.. sip:method-description::
    :status: todo
    :pysig: 787ad3d0f6e2063950bbbf6e050908f3
    :realsig: (QStringView)
    :digest: d89557e0f0412d2190d98a268600e77e

Attempts to load a backend whose name matches *backend* (case insensitively).

Returns ``true`` if it managed to load the requested backend or if it was already loaded. Returns ``false`` otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.instance`.
