.. sip:class-description::
    :status: todo
    :brief: QIODevice interface for a QByteArray
    :digest: 34180317487ad00e982011c5d9cd62c7

The :sip:ref:`~PyQt6.QtCore.QBuffer` class provides a :sip:ref:`~PyQt6.QtCore.QIODevice` interface for a :sip:ref:`~PyQt6.QtCore.QByteArray`.

:sip:ref:`~PyQt6.QtCore.QBuffer` allows you to access a :sip:ref:`~PyQt6.QtCore.QByteArray` using the :sip:ref:`~PyQt6.QtCore.QIODevice` interface. The :sip:ref:`~PyQt6.QtCore.QByteArray` is treated just as a standard random-accessed file. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-buffer-buffer.py
    :lines: 60-69

By default, an internal :sip:ref:`~PyQt6.QtCore.QByteArray` buffer is created for you when you create a :sip:ref:`~PyQt6.QtCore.QBuffer`. You can access this buffer directly by calling :sip:ref:`~PyQt6.QtCore.QBuffer.buffer`. You can also use :sip:ref:`~PyQt6.QtCore.QBuffer` with an existing :sip:ref:`~PyQt6.QtCore.QByteArray` by calling :sip:ref:`~PyQt6.QtCore.QBuffer.setBuffer`, or by passing your array to :sip:ref:`~PyQt6.QtCore.QBuffer`'s constructor.

Call :sip:ref:`~PyQt6.QtCore.QBuffer.open` to open the buffer. Then call write() or putChar() to write to the buffer, and read(), readLine(), readAll(), or getChar() to read from it. :sip:ref:`~PyQt6.QtCore.QBuffer.size` returns the current size of the buffer, and you can seek to arbitrary positions in the buffer by calling :sip:ref:`~PyQt6.QtCore.QBuffer.seek`. When you are done with accessing the buffer, call :sip:ref:`~PyQt6.QtCore.QBuffer.close`.

The following code snippet shows how to write data to a :sip:ref:`~PyQt6.QtCore.QByteArray` using :sip:ref:`~PyQt6.QtCore.QDataStream` and :sip:ref:`~PyQt6.QtCore.QBuffer`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-buffer-buffer.py
    :lines: 76-81

Effectively, we convert the application's QPalette into a byte array. Here's how to read the data from the :sip:ref:`~PyQt6.QtCore.QByteArray`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-buffer-buffer.py
    :lines: 90-95

:sip:ref:`~PyQt6.QtCore.QTextStream` and :sip:ref:`~PyQt6.QtCore.QDataStream` also provide convenience constructors that take a :sip:ref:`~PyQt6.QtCore.QByteArray` and that create a :sip:ref:`~PyQt6.QtCore.QBuffer` behind the scenes.

:sip:ref:`~PyQt6.QtCore.QBuffer` emits readyRead() when new data has arrived in the buffer. By connecting to this signal, you can use :sip:ref:`~PyQt6.QtCore.QBuffer` to store temporary data before processing it. :sip:ref:`~PyQt6.QtCore.QBuffer` also emits bytesWritten() every time new data has been written to the buffer.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtCore.QDataStream`, :sip:ref:`~PyQt6.QtCore.QTextStream`, :sip:ref:`~PyQt6.QtCore.QByteArray`.
