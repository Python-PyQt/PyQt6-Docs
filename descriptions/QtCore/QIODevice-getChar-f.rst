.. sip:method-description::
    :status: todo
    :pysig: 90d3ce45dd716b35f03e46a97c1f5b58
    :realsig: (char*)
    :digest: efcda268fcc59ffdb586045dd043958e

Reads one character from the device and stores it in *c*. If *c* is ``nullptr``, the character is discarded. Returns ``true`` on success; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.read`, :sip:ref:`~PyQt6.QtCore.QIODevice.putChar`, :sip:ref:`~PyQt6.QtCore.QIODevice.ungetChar`.
