.. sip:method-description::
    :status: todo
    :pysig: 28ebbf48eaa8eb1de530ed7bc03433c3
    :realsig: (QNearFieldTarget::AccessMethod)
    :digest: 25c1787754d0abce346c90f75d20c927

Starts detecting targets and returns ``true`` if target detection is successfully started; otherwise returns ``false``. Causes the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` signal to be emitted when a target is within proximity. Only tags with the given *accessMethod* will be delivered. Active detection continues until :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` has been called.

To detect targets with a different *accessMethod*, :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` must be called first.

**Note:** On iOS it is impossible to start target detection for both NdefAccess and TagTypeSpecificAccess at the same time. So if AnyAccess is selected, NdefAccess will be used instead.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection`.
