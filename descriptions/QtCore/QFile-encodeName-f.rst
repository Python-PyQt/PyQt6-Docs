.. sip:method-description::
    :status: todo
    :pysig: 6b879fccf236c977adcd06b596163a08
    :realsig: (const QString&)
    :digest: 1f5e1694cc09a1af40c264de785dcc7c

Converts *fileName* to an 8-bit encoding that you can use in native APIs. On Windows, the encoding is the one from active Windows (ANSI) codepage. On other platforms, this is UTF-8, for macOS in decomposed form (NFD).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.decodeName`.
