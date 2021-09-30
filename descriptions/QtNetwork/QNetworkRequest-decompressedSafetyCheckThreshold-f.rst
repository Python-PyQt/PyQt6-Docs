.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: f7796eaf58e8e548e40e8f62a553c252

Returns the threshold for archive bomb checks.

If the decompressed size of a reply is smaller than this, Qt will simply decompress it, without further checking.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setDecompressedSafetyCheckThreshold`.
