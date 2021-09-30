.. sip:signal-description::
    :status: todo
    :pysig: d948954506ef8daad5023e67d66e3320
    :realsig: (QNearFieldTarget*)
    :digest: faa5f2862c695a92f3b40ba1631975de

This signal is emitted whenever a target moves out of proximity. The *target* parameter represents the lost target.

Do not delete *target* from the slot connected to this signal, instead use deleteLater().

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.disconnected`.
