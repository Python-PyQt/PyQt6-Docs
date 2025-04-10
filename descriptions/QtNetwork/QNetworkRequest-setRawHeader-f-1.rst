.. sip:method-description::
    :status: todo
    :pysig: 9a01ca953cb072293976de4f13623118
    :realsig: (const QByteArray&, const QByteArray&)
    :digest: 87b7ce086d893e1c598f3f84286c4389

Sets the header *headerName* to be of value *headerValue*. If *headerName* corresponds to a known header (see :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`), the raw format will be parsed and the corresponding "cooked" header will be set as well.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkrequest.py
    :lines: 54-54

will also set the known header :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders.LastModifiedHeader` to be the :sip:ref:`~PyQt6.QtCore.QDateTime` object of the parsed date.

**Note:** Setting the same header twice overrides the previous setting. To accomplish the behaviour of multiple HTTP headers of the same name, you should concatenate the two values, separating them with a comma (",") and set one single raw header.

**Note:** Since Qt 6.8, the header field names are normalized by converting them to lowercase.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders.KnownHeaders`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.hasRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.rawHeader`.
