.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: e3b165e6a46917fbc2506b2169380cbb

Creates a :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` object that will write the stream to *device*. The device must be opened before the first :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.append` call is made. This constructor can be used with any class that derives from :sip:ref:`~PyQt6.QtCore.QIODevice`, such as :sip:ref:`~PyQt6.QtCore.QFile`, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ or QTcpSocket.

:sip:ref:`~PyQt6.QtCore.QCborStreamWriter` has no buffering, so every :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.append` call will result in one or more calls to the device's :sip:ref:`~PyQt6.QtCore.QIODevice.write` method.

The following example writes an empty map to a file:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 78-81

:sip:ref:`~PyQt6.QtCore.QCborStreamWriter` does not take ownership of *device*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.device`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.setDevice`.
