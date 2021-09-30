.. sip:class-description::
    :status: todo
    :brief: Interface for communicating with a target device
    :digest: 0f1c9325c05117c409f0fef0256d9f3e

The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget` class provides an interface for communicating with a target device.

:sip:ref:`~PyQt6.QtNfc.QNearFieldTarget` provides a generic interface for communicating with an NFC target device. Both NFC Forum devices and NFC Forum Tag targets are supported by this class. All target specific classes subclass this class.

The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.type` function can be used to get the type of the target device. The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.uid` function returns the unique identifier of the target. The AccessMethods flags returns from the :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.accessMethods` function can be tested to determine which access methods are supported by the target.

If the target supports :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.AccessMethod.NdefAccess`, :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.hasNdefMessage` can be called to test if the target has a stored NDEF message, :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.readNdefMessages` and :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.writeNdefMessages` functions can be used to get and set the NDEF message.

If the target supports :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.AccessMethod.TagTypeSpecificAccess`, :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.sendCommand` can be used to send a single proprietary command to the target and retrieve the response.
