.. sip:method-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (qsizetype)
    :digest: 4058957f5c75b1c5798676f4487c4fbf

Modifies this byte array to start at position *pos*, extending to its end, and returns a reference to this byte array.

**Note:** The behavior is undefined if *pos* < 0 or *pos* > :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.sliced`, :sip:ref:`~PyQt6.QtCore.QByteArray.first`, :sip:ref:`~PyQt6.QtCore.QByteArray.last`, :sip:ref:`~PyQt6.QtCore.QByteArray.chopped`, :sip:ref:`~PyQt6.QtCore.QByteArray.chop`, :sip:ref:`~PyQt6.QtCore.QByteArray.truncate`.
