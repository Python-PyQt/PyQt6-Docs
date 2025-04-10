.. sip:class-description::
    :status: todo
    :brief: Interface for communicating with a target device
    :digest: 2d4dcafa6da68595b22f0261c95a8d16

The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget` class provides an interface for communicating with a target device.

:sip:ref:`~PyQt6.QtNfc.QNearFieldTarget` provides a generic interface for communicating with an NFC target device. Both NFC Forum devices and NFC Forum Tag targets are supported by this class. All target specific classes subclass this class.

The `type() <https://doc.qt.io/qt-6/qml-geoshape.html#type>`_ function can be used to get the type of the target device. The uid() function returns the unique identifier of the target. The AccessMethods flags returns from the accessMethods() function can be tested to determine which access methods are supported by the target.

If the target supports NdefAccess, hasNdefMessage() can be called to test if the target has a stored NDEF message, readNdefMessages() and writeNdefMessages() functions can be used to get and set the NDEF message.

If the target supports TagTypeSpecificAccess, sendCommand() can be used to send a single proprietary command to the target and retrieve the response.
