.. sip:signal-description::
    :status: todo
    :pysig: d948954506ef8daad5023e67d66e3320
    :realsig: (QNearFieldTarget*)
    :digest: c75ec61c86e7b161c2328f87b2bd8f9c

This signal is emitted whenever a target is detected. The *target* parameter represents the detected target.

This signal will be emitted for all detected targets.

:sip:ref:`~PyQt6.QtNfc.QNearFieldManager` maintains ownership of *target*, however, it will not be destroyed until the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager` destructor is called. Ownership may be transferred by calling setParent().

Do not delete *target* from the slot connected to this signal, instead call deleteLater().

**Note:** that if *target* is deleted before it moves out of proximity the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetLost` signal will not be emitted.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetLost`.
