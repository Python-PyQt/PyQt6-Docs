.. sip:method-description::
    :status: todo
    :pysig: edfc6ad7e4c99d0040585a75d6eaae73
    :realsig: (const QByteArray&,const QByteArray&)
    :digest: 00a9c0fd9f29a293eb263ced96158ab1

Sets the header *headerName* to be of value *headerValue*. If *headerName* corresponds to a known header (see :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`), the raw format will be parsed and the corresponding "cooked" header will be set as well.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkrequest.py
    :lines: 54-54

will also set the known header :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders.LastModifiedHeader` to be the :sip:ref:`~PyQt6.QtCore.QDateTime` object of the parsed date.

**Note:** Setting the same header twice overrides the previous setting. To accomplish the behaviour of multiple HTTP headers of the same name, you should concatenate the two values, separating them with a comma (",") and set one single raw header.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders.KnownHeaders`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.hasRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.rawHeader`.
