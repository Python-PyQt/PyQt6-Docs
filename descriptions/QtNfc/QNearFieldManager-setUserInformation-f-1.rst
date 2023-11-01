.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: ca29e193fc884f726a47048961a03f0b

Sets the message shown to the user by the system. If the target detection is running the *message* will be updated immediately and can be used as a progress message. The last message set before a call to :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.startTargetDetection` without an error message is used as a success message. If the target detection is not running the *message* will be used as the initial message when the next detection is started. By default no message is shown to the user.

**Note:** Currently, this function only has an effect on iOS because a popup is shown by the system during the scan. On iOS, this *message* is mapped to the alert message which is shown upon successful completion of the scan. Other platforms will ignore *message*.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.startTargetDetection`, :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection`.
