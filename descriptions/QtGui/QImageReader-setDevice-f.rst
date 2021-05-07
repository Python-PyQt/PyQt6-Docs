.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: be479bd9dd2de55d664ac5bcbb8ebccf

Sets :sip:ref:`~PyQt6.QtGui.QImageReader`'s device to *device*. If a device has already been set, the old device is removed from :sip:ref:`~PyQt6.QtGui.QImageReader` and is otherwise left unchanged.

If the device is not already open, :sip:ref:`~PyQt6.QtGui.QImageReader` will attempt to open the device in :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.ReadOnly` mode by calling open(). Note that this does not work for certain devices, such as :sip:ref:`~PyQt6.QtCore.QProcess`, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` and :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, where more logic is required to open the device.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.device`, :sip:ref:`~PyQt6.QtGui.QImageReader.setFileName`.
