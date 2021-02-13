.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: da75b0c9d521aba0c52e44a154b95aa8

Sets the writer's device to the *device* specified. If a device has already been set, the old device is removed but otherwise left unchanged.

If the device is not already open, :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter` will attempt to open the device in :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.WriteOnly` mode by calling open().

**Note:** This will not work for certain devices, such as `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` and :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, where some configuration is required before the device can be opened.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.device`, :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.setFileName`.
