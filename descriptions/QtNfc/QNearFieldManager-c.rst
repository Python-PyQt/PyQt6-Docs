.. sip:class-description::
    :status: todo
    :brief: Access to notifications for NFC events
    :digest: 00c394ce175f801e868415dbcc9613bc

The :sip:ref:`~PyQt6.QtNfc.QNearFieldManager` class provides access to notifications for NFC events.

NFC Forum devices support two modes of communications. The first mode, peer-to-peer communications, is used to communicate between two NFC Forum devices. The second mode, master/slave communications, is used to communicate between an NFC Forum device and an NFC Forum Tag or Contactless Card. The :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` signal is emitted when a target device enters communications range. Communications can be initiated from the slot connected to this signal.

NFC Forum devices generally operate as the master in master/slave communications. Some devices are also capable of operating as the slave, so called Card Emulation mode. In this mode the local NFC device emulates a NFC Forum Tag or Contactless Card.

Applications can connect to the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` and :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetLost` signals to get notified when an NFC Forum Tag enters or leaves proximity. Before these signals are emitted target detection must be started with the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.startTargetDetection` function. Target detection can be stopped with the :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` function. When the target is no longer required the target should be deleted as other applications may be blocked from accessing the target.

.. _qnearfieldmanager-nfc-on-linux:

NFC on Linux
^^^^^^^^^^^^

The `Linux NFC project <https://github.com/linux-nfc/neard>`_ provides software to support NFC on Linux platforms. The neard daemon will allow access to the supported hardware via DBus interfaces. :sip:ref:`~PyQt6.QtNfc` requires neard version 0.14 which can be built from source or installed via the appropriate Linux package manager. Not all API features are currently supported. To allow :sip:ref:`~PyQt6.QtNfc` to access the DBus interfaces the neard daemon has to be running. In case of problems debug output can be enabled by enabling categorized logging for 'qt.nfc.neard'.
