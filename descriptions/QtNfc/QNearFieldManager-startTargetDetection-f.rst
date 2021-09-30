.. sip:method-description::
    :status: todo
    :pysig: 28ebbf48eaa8eb1de530ed7bc03433c3
    :realsig: (QNearFieldTarget::AccessMethod)
    :digest: 55db45e434011fb7ed08f02626a7c42f

Starts detecting targets and returns ``true`` if target detection is successfully started; otherwise returns ``false``. Causes the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` signal to be emitted when a target is within proximity. Only tags with the given *accessMethod* will be delivered. Active detection continues until :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` has been called.

To detect targets with a different *accessMethod*, :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` must be called first.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection`.
