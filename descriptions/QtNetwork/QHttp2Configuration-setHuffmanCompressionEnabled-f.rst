.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 019c0cb1928fbf795af2611c6e857a57

If *enable* is ``true``, HPACK compression will additionally compress string using the Huffman coding. Enabled by default.

**Note:** This parameter only affects 'HEADERS' frames that :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` is sending.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttp2Configuration.huffmanCompressionEnabled`.
