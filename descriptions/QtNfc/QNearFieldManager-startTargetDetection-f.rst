.. sip:method-description::
    :status: todo
    :pysig: 28ebbf48eaa8eb1de530ed7bc03433c3
    :realsig: (QNearFieldTarget::AccessMethod)
    :digest: 5fecd0ddd5f55dee2ac8fba01612a82c

Starts detecting targets and returns ``true`` if target detection started successfully; otherwise returns ``false``. Causes the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` signal to be emitted when a target is within proximity. Only tags with the given *accessMethod* will be reported. Target detection continues until :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` is called.

To detect targets with a different *accessMethod*, :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` must be called first.

**Note:** On iOS, it is impossible to start target detection for both NdefAccess and TagTypeSpecificAccess at the same time. So if AnyAccess is selected, NdefAccess will be used instead.

**Note:** On platforms using neard, target detection will stop as soon as a tag has been detected.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection`.
