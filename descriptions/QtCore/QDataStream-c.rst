.. sip:class-description::
    :status: todo
    :brief: Serialization of binary data to a QIODevice
    :digest: 0eb2e8e04769367257cb75d8b1e15eba

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

Each item written to the stream is written in a predefined binary format that varies depending on the item's type. Supported Qt types include :sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.QDateTime`, :sip:ref:`~PyQt6.QtGui.QFont`, :sip:ref:`~PyQt6.QtGui.QPixmap`, QString, :sip:ref:`~PyQt6.QtCore.QVariant` and many others. For the complete list of all Qt types supporting data streaming see `Serializing Qt Data Types <https://doc.qt.io/qt-6/datastreamformat.html>`_.

For integers it is best to always cast to a Qt integer type for writing, and to read back into the same Qt integer type. This ensures that you get integers of the size you want and insulates you from compiler and platform differences.

Enumerations can be serialized through :sip:ref:`~PyQt6.QtCore.QDataStream` without the need of manually defining streaming operators. Enum classes are serialized using the declared size.

The initial I/O device is usually set in the constructor, but can be changed with :sip:ref:`~PyQt6.QtCore.QDataStream.setDevice`. If you've reached the end of the data (or if there is no I/O device set) :sip:ref:`~PyQt6.QtCore.QDataStream.atEnd` will return true.

.. _qdatastream-serializing-containers-and-strings:

Serializing containers and strings
----------------------------------

The serialization format is a length specifier first, then *l* bytes of data. The length specifier is one quint32 if the version is less than 6.7 or if the number of elements is less than 0xfffffffe (2^32 -2). Otherwise there is an extend value 0xfffffffe followed by one quint64 with the actual value. In addition for containers that support isNull(), it is encoded as a single quint32 with all bits set and no data.

To take one example, if the string size fits into 32 bits, a ``char \*`` string is written as a 32-bit integer equal to the length of the string, including the '\\0' byte, followed by all the characters of the string, including the '\\0' byte. If the string size is greater, the value 0xffffffffe is written as a marker of an extended size, followed by 64 bits of the actual size. When reading a ``char \*`` string, 4 bytes are read first. If the value is not equal to 0xffffffffe (the marker of extended size), then these 4 bytes are treated as the 32 bit size of the string. Otherwise, the next 8 bytes are read and treated as a 64 bit size of the string. Then, all the characters for the ``char \*`` string, including the '\\0' terminator, are read.

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

You can select which byte order to use when serializing data. The default setting is big-endian (MSB first). Changing it to little-endian breaks the portability (unless the reader also changes to little-endian). We recommend keeping this setting unless you have special requirements.

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

.. _qdatastream-corruption-and-security:

Corruption and Security
-----------------------

:sip:ref:`~PyQt6.QtCore.QDataStream` is not resilient against corrupted data inputs and should therefore not be used for security-sensitive situations, even when using transactions. Transactions will help determine if a valid input can currently be decoded with the data currently available on an asynchronous device, but will assume that the data that is available is correctly formed.

Additionally, many :sip:ref:`~PyQt6.QtCore.QDataStream` demarshalling operators will allocate memory based on information found in the stream. Those operators perform no verification on whether the requested amount of memory is reasonable or if it is compatible with the amount of data available in the stream (example: demarshalling a :sip:ref:`~PyQt6.QtCore.QByteArray` or QString may see the request for allocation of several gigabytes of data).

:sip:ref:`~PyQt6.QtCore.QDataStream` should not be used on content whose provenance cannot be trusted. Applications should be designed to attempt to decode only streams whose provenance is at least as trustworthy as that of the application itself or its plugins.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream`, :sip:ref:`~PyQt6.QtCore.QVariant`.
