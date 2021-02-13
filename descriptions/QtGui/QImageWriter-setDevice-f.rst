.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: d768e8955eda3d51e7cf8d48a44c3a4d

Sets :sip:ref:`~PyQt6.QtGui.QImageWriter`'s device to *device*. If a device has already been set, the old device is removed from :sip:ref:`~PyQt6.QtGui.QImageWriter` and is otherwise left unchanged.

If the device is not already open, :sip:ref:`~PyQt6.QtGui.QImageWriter` will attempt to open the device in :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.WriteOnly` mode by calling open(). Note that this does not work for certain devices, such as `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_, QTcpSocket and QUdpSocket, where more logic is required to open the device.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.device`, :sip:ref:`~PyQt6.QtGui.QImageWriter.setFileName`.
