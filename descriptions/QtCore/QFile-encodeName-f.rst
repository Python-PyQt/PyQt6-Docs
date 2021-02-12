.. sip:method-description::
    :status: todo
    :pysig: b2a1c3086695add31455bfea8040aff8
    :realsig: (const QString&)
    :digest: 1f5e1694cc09a1af40c264de785dcc7c

Converts *fileName* to the local 8-bit encoding determined by the user's locale. This is sufficient for file names that the user chooses. File names hard-coded into the application should only use 7-bit ASCII filename characters.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.decodeName`.
