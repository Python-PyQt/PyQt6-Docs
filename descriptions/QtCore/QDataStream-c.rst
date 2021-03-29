.. sip:class-description::
    :status: todo
    :brief: Serialization of binary data to a QIODevice
    :digest: 49ca38683af4946e8e47e850fa1124c8

The :sip:ref:`~PyQt6.QtCore.QDataStream` class provides serialization of binary data to a :sip:ref:`~PyQt6.QtCore.QIODevice`.

A data stream is a binary stream of encoded information which is 100% independent of the host computer's operating system, CPU or byte order. For example, a data stream that is written by a PC under Windows can be read by a Sun SPARC running Solaris.

You can also use a data stream to read/write raw unencoded binary data. If you want a "parsing" input stream, see :sip:ref:`~PyQt6.QtCore.QTextStream`.

The :sip:ref:`~PyQt6.QtCore.QDataStream` class implements the serialization of C++'s basic data types, like ``char``, ``short``, ``int``, ``char \*``, etc. Serialization of more complex data is accomplished by breaking up the data into primitive units.

A data stream cooperates closely with a :sip:ref:`~PyQt6.QtCore.QIODevice`. A :sip:ref:`~PyQt6.QtCore.QIODevice` represents an input/output medium one can read data from and write data to. The :sip:ref:`~PyQt6.QtCore.QFile` class is an example of an I/O device.

Example (write binary data to a stream):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdatastream.py
    :lines: 57-61

Example (read binary data from a stream):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdatastream.py
    :lines: 66-71

Each item written to the stream is written in a predefined binary format that varies depending on the item's type. Supported Qt types include :sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.QDateTime`, `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_, :sip:ref:`~PyQt6.QtGui.QPixmap`, QString, `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ and many others. For the complete list of all Qt types supporting data streaming see `Serializing Qt Data Types <https://doc.qt.io/qt-6/datastreamformat.html>`_.

For integers it is best to always cast to a Qt integer type for writing, and to read back into the same Qt integer type. This ensures that you get integers of the size you want and insulates you from compiler and platform differences.

Enumerations can be serialized through :sip:ref:`~PyQt6.QtCore.QDataStream` without the need of manually defining streaming operators. Enum classes are serialized using the declared size.

To take one example, a ``char \*`` string is written as a 32-bit integer equal to the length of the string including the '\\0' byte, followed by all the characters of the string including the '\\0' byte. When reading a ``char \*`` string, 4 bytes are read to create the 32-bit length value, then that many characters for the ``char \*`` string including the '\\0' terminator are read.

The initial I/O device is usually set in the constructor, but can be changed with :sip:ref:`~PyQt6.QtCore.QDataStream.setDevice`. If you've reached the end of the data (or if there is no I/O device set) :sip:ref:`~PyQt6.QtCore.QDataStream.atEnd` will return true.

.. _qdatastream-versioning:

Versioning
----------

:sip:ref:`~PyQt6.QtCore.QDataStream`'s binary format has evolved since Qt 1.0, and is likely to continue evolving to reflect changes done in Qt. When inputting or outputting complex types, it's very important to make sure that the same version of the stream (\ :sip:ref:`~PyQt6.QtCore.QDataStream.version`) is used for reading and writing. If you need both forward and backward compatibility, you can hardcode the version number in the application:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdatastream.py
    :lines: 76-76

If you are producing a new binary data format, such as a file format for documents created by your application, you could use a :sip:ref:`~PyQt6.QtCore.QDataStream` to write the data in a portable format. Typically, you would write a brief header containing a magic string and a version number to give yourself room for future expansion. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdatastream.py
    :lines: 81-92

Then read it in with:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdatastream.py
    :lines: 97-124

You can select which byte order to use when serializing data. The default setting is big endian (MSB first). Changing it to little endian breaks the portability (unless the reader also changes to little endian). We recommend keeping this setting unless you have special requirements.

.. _qdatastream-raw:

.. _qdatastream-reading-and-writing-raw-binary-data:

Reading and Writing Raw Binary Data
-----------------------------------

You may wish to read/write your own raw binary data to/from the data stream directly. Data may be read from the stream into a preallocated ``char \*`` using :sip:ref:`~PyQt6.QtCore.QDataStream.readRawData`. Similarly data can be written to the stream using :sip:ref:`~PyQt6.QtCore.QDataStream.writeRawData`. Note that any encoding/decoding of the data must be done by you.

A similar pair of functions is :sip:ref:`~PyQt6.QtCore.QDataStream.readBytes` and :sip:ref:`~PyQt6.QtCore.QDataStream.writeBytes`. These differ from their *raw* counterparts as follows: :sip:ref:`~PyQt6.QtCore.QDataStream.readBytes` reads a quint32 which is taken to be the length of the data to be read, then that number of bytes is read into the preallocated ``char \*``; :sip:ref:`~PyQt6.QtCore.QDataStream.writeBytes` writes a quint32 containing the length of the data, followed by the data. Note that any encoding/decoding of the data (apart from the length quint32) must be done by you.

.. _qdatastream-reading-and-writing-qt-collection-classes:

Reading and Writing Qt Collection Classes
-----------------------------------------

The Qt container classes can also be serialized to a :sip:ref:`~PyQt6.QtCore.QDataStream`. These include QList, QSet, QHash, and QMap. The stream operators are declared as non-members of the classes.

.. _qdatastream-serializing-qt-classes:

.. _qdatastream-reading-and-writing-other-qt-classes:

Reading and Writing Other Qt Classes
------------------------------------

In addition to the overloaded stream operators documented here, any Qt classes that you might want to serialize to a :sip:ref:`~PyQt6.QtCore.QDataStream` will have appropriate stream operators declared as non-member of the class:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qdatastream.py
    :lines: 54-55

For example, here are the stream operators declared as non-members of the :sip:ref:`~PyQt6.QtGui.QImage` class:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qdatastream.py
    :lines: 59-60

To see if your favorite Qt class has similar stream operators defined, check the **Related Non-Members** section of the class's documentation page.

.. _qdatastream-using-read-transactions:

Using Read Transactions
-----------------------

When a data stream operates on an asynchronous device, the chunks of data can arrive at arbitrary points in time. The :sip:ref:`~PyQt6.QtCore.QDataStream` class implements a transaction mechanism that provides the ability to read the data atomically with a series of stream operators. As an example, you can handle incomplete reads from a socket by using a transaction in a slot connected to the readyRead() signal:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdatastream.py
    :lines: 134-140

If no full packet is received, this code restores the stream to the initial position, after which you need to wait for more data to arrive.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream`, `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_.
