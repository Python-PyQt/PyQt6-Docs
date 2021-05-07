.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: d437f1f6e332fe0c646d7b29a23a8892

Sets the writer's device to the *device* specified. If a device has already been set, the old device is removed but otherwise left unchanged.

If the device is not already open, :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter` will attempt to open the device in :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.WriteOnly` mode by calling open().

**Note:** This will not work for certain devices, such as :sip:ref:`~PyQt6.QtCore.QProcess`, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` and :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, where some configuration is required before the device can be opened.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.device`, :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.setFileName`.
