.. sip:class-description::
    :status: todo
    :brief: The base interface class of all I/O devices in Qt
    :digest: be9134992d7514f24a0d0c1138e701f7

The :sip:ref:`~PyQt6.QtCore.QIODevice` class is the base interface class of all I/O devices in Qt.

:sip:ref:`~PyQt6.QtCore.QIODevice` provides both a common implementation and an abstract interface for devices that support reading and writing of blocks of data, such as :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtCore.QBuffer` and :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`. :sip:ref:`~PyQt6.QtCore.QIODevice` is abstract and cannot be instantiated, but it is common to use the interface it defines to provide device-independent I/O features. For example, Qt's XML classes operate on a :sip:ref:`~PyQt6.QtCore.QIODevice` pointer, allowing them to be used with various devices (such as files and buffers).

Before accessing the device, :sip:ref:`~PyQt6.QtCore.QIODevice.open` must be called to set the correct OpenMode (such as :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.ReadOnly` or :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.ReadWrite`). You can then write to the device with :sip:ref:`~PyQt6.QtCore.QIODevice.write` or :sip:ref:`~PyQt6.QtCore.QIODevice.putChar`, and read by calling either :sip:ref:`~PyQt6.QtCore.QIODevice.read`, :sip:ref:`~PyQt6.QtCore.QIODevice.readLine`, or :sip:ref:`~PyQt6.QtCore.QIODevice.readAll`. Call :sip:ref:`~PyQt6.QtCore.QIODevice.close` when you are done with the device.

:sip:ref:`~PyQt6.QtCore.QIODevice` distinguishes between two types of devices: random-access devices and sequential devices.

* Random-access devices support seeking to arbitrary positions using :sip:ref:`~PyQt6.QtCore.QIODevice.seek`. The current position in the file is available by calling :sip:ref:`~PyQt6.QtCore.QIODevice.pos`. :sip:ref:`~PyQt6.QtCore.QFile` and :sip:ref:`~PyQt6.QtCore.QBuffer` are examples of random-access devices.

* Sequential devices don't support seeking to arbitrary positions. The data must be read in one pass. The functions :sip:ref:`~PyQt6.QtCore.QIODevice.pos` and :sip:ref:`~PyQt6.QtCore.QIODevice.size` don't work for sequential devices. :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` and `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ are examples of sequential devices.

You can use :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential` to determine the type of device.

:sip:ref:`~PyQt6.QtCore.QIODevice` emits :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` when new data is available for reading; for example, if new data has arrived on the network or if additional data is appended to a file that you are reading from. You can call :sip:ref:`~PyQt6.QtCore.QIODevice.bytesAvailable` to determine the number of bytes that are currently available for reading. It's common to use :sip:ref:`~PyQt6.QtCore.QIODevice.bytesAvailable` together with the :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` signal when programming with asynchronous devices such as :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, where fragments of data can arrive at arbitrary points in time. :sip:ref:`~PyQt6.QtCore.QIODevice` emits the :sip:ref:`~PyQt6.QtCore.QIODevice.bytesWritten` signal every time a payload of data has been written to the device. Use :sip:ref:`~PyQt6.QtCore.QIODevice.bytesToWrite` to determine the current amount of data waiting to be written.

Certain subclasses of :sip:ref:`~PyQt6.QtCore.QIODevice`, such as :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` and `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_, are asynchronous. This means that I/O functions such as :sip:ref:`~PyQt6.QtCore.QIODevice.write` or :sip:ref:`~PyQt6.QtCore.QIODevice.read` always return immediately, while communication with the device itself may happen when control goes back to the event loop. :sip:ref:`~PyQt6.QtCore.QIODevice` provides functions that allow you to force these operations to be performed immediately, while blocking the calling thread and without entering the event loop. This allows :sip:ref:`~PyQt6.QtCore.QIODevice` subclasses to be used without an event loop, or in a separate thread:

* :sip:ref:`~PyQt6.QtCore.QIODevice.waitForReadyRead` - This function suspends operation in the calling thread until new data is available for reading.

* :sip:ref:`~PyQt6.QtCore.QIODevice.waitForBytesWritten` - This function suspends operation in the calling thread until one payload of data has been written to the device.

* waitFor....() - Subclasses of :sip:ref:`~PyQt6.QtCore.QIODevice` implement blocking functions for device-specific operations. For example, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ has a function called :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted` which suspends operation in the calling thread until the process has started.

Calling these functions from the main, GUI thread, may cause your user interface to freeze. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qiodevice.py
    :lines: 54-63

By subclassing :sip:ref:`~PyQt6.QtCore.QIODevice`, you can provide the same interface to your own I/O devices. Subclasses of :sip:ref:`~PyQt6.QtCore.QIODevice` are only required to implement the protected :sip:ref:`~PyQt6.QtCore.QIODevice.readData` and :sip:ref:`~PyQt6.QtCore.QIODevice.writeData` functions. :sip:ref:`~PyQt6.QtCore.QIODevice` uses these functions to implement all its convenience functions, such as :sip:ref:`~PyQt6.QtCore.QIODevice.getChar`, :sip:ref:`~PyQt6.QtCore.QIODevice.readLine` and :sip:ref:`~PyQt6.QtCore.QIODevice.write`. :sip:ref:`~PyQt6.QtCore.QIODevice` also handles access control for you, so you can safely assume that the device is opened in write mode if :sip:ref:`~PyQt6.QtCore.QIODevice.writeData` is called.

Some subclasses, such as :sip:ref:`~PyQt6.QtCore.QFile` and :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, are implemented using a memory buffer for intermediate storing of data. This reduces the number of required device accessing calls, which are often very slow. Buffering makes functions like :sip:ref:`~PyQt6.QtCore.QIODevice.getChar` and :sip:ref:`~PyQt6.QtCore.QIODevice.putChar` fast, as they can operate on the memory buffer instead of directly on the device itself. Certain I/O operations, however, don't work well with a buffer. For example, if several users open the same device and read it character by character, they may end up reading the same data when they meant to read a separate chunk each. For this reason, :sip:ref:`~PyQt6.QtCore.QIODevice` allows you to bypass any buffering by passing the Unbuffered flag to :sip:ref:`~PyQt6.QtCore.QIODevice.open`. When subclassing :sip:ref:`~PyQt6.QtCore.QIODevice`, remember to bypass any buffer you may use when the device is open in Unbuffered mode.

Usually, the incoming data stream from an asynchronous device is fragmented, and chunks of data can arrive at arbitrary points in time. To handle incomplete reads of data structures, use the transaction mechanism implemented by :sip:ref:`~PyQt6.QtCore.QIODevice`. See :sip:ref:`~PyQt6.QtCore.QIODevice.startTransaction` and related functions for more details.

Some sequential devices support communicating via multiple channels. These channels represent separate streams of data that have the property of independently sequenced delivery. Once the device is opened, you can determine the number of channels by calling the :sip:ref:`~PyQt6.QtCore.QIODevice.readChannelCount` and :sip:ref:`~PyQt6.QtCore.QIODevice.writeChannelCount` functions. To switch between channels, call :sip:ref:`~PyQt6.QtCore.QIODevice.setCurrentReadChannel` and :sip:ref:`~PyQt6.QtCore.QIODevice.setCurrentWriteChannel`, respectively. :sip:ref:`~PyQt6.QtCore.QIODevice` also provides additional signals to handle asynchronous communication on a per-channel basis.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBuffer`, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`.
