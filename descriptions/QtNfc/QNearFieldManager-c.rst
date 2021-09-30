.. sip:class-description::
    :status: todo
    :brief: Access to notifications for NFC events
    :digest: 4fd64d9d35b64d71f329a2e8f32453e1

The :sip:ref:`~PyQt6.QtNfc.QNearFieldManager` class provides access to notifications for NFC events.

NFC Forum devices support two modes of communications. The first mode, peer-to-peer communications, is used to communicate between two NFC Forum devices. The second mode, master/slave communications, is used to communicate between an NFC Forum device and an NFC Forum Tag or Contactless Card. The :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` signal is emitted when a target device enters communications range. Communications can be initiated from the slot connected to this signal.

NFC Forum devices generally operate as the master in master/slave communications. Some devices are also capable of operating as the slave, so called Card Emulation mode. In this mode the local NFC device emulates a NFC Forum Tag or Contactless Card.

Applications can connect to the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` and :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetLost` signals to get notified when an NFC Forum Tag enters or leaves proximity. Before these signals are emitted target detection must be started with the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.startTargetDetection` function. Target detection can be stopped with the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` function. When the target is no longer required the target should be deleted as other applications may be blocked from accessing the target.
