.. sip:method-description::
    :status: todo
    :pysig: 5d90a6523e08a4c90a3212318eb9d8e3
    :realsig: (const QString&)
    :digest: 1f5e1694cc09a1af40c264de785dcc7c

Converts *fileName* to an 8-bit encoding that you can use in native APIs. On Windows, the encoding is the one from active Windows (ANSI) codepage. On other platforms, this is UTF-8, for macOS in decomposed form (NFD).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.decodeName`.
