.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: b914f8b91ccce1a4765f194a2a4b99f1

If *generate* is true and a UTF encoding is used, :sip:ref:`~PyQt6.QtCore.QTextStream` will insert the BOM (Byte Order Mark) before any data has been written to the device. If *generate* is false, no BOM will be inserted. This function must be called before any data is written. Otherwise, it does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.generateByteOrderMark`, :sip:ref:`~PyQt6.QtCore.Qt.bom`.
