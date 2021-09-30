.. sip:class-description::
    :status: todo
    :brief: Array of bytes
    :digest: 4932f85f57f3884bf76993cc64500407

The :sip:ref:`~PyQt6.QtCore.QByteArray` class provides an array of bytes.

:sip:ref:`~PyQt6.QtCore.QByteArray` can be used to store both raw bytes (including '\\0's) and traditional 8-bit '\\0'-terminated strings. Using :sip:ref:`~PyQt6.QtCore.QByteArray` is much more convenient than using ``const char \*``. Behind the scenes, it always ensures that the data is followed by a '\\0' terminator, and uses `implicit sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_ (copy-on-write) to reduce memory usage and avoid needless copying of data.

In addition to :sip:ref:`~PyQt6.QtCore.QByteArray`, Qt also provides the QString class to store string data. For most purposes, QString is the class you want to use. It understands its content as Unicode text (encoded using UTF-16) where :sip:ref:`~PyQt6.QtCore.QByteArray` aims to avoid assumptions about the encoding or semantics of the bytes it stores (aside from a few legacy cases where it uses ASCII). Furthermore, QString is used throughout in the Qt API. The two main cases where :sip:ref:`~PyQt6.QtCore.QByteArray` is appropriate are when you need to store raw binary data, and when memory conservation is critical (e.g., with Qt for Embedded Linux).

One way to initialize a :sip:ref:`~PyQt6.QtCore.QByteArray` is simply to pass a ``const char \*`` to its constructor. For example, the following code creates a byte array of size 5 containing the data "Hello":

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 58-58

Although the :sip:ref:`~PyQt6.QtCore.QByteArray.size` is 5, the byte array also maintains an extra '\\0' byte at the end so that if a function is used that asks for a pointer to the underlying data (e.g. a call to :sip:ref:`~PyQt6.QtCore.QByteArray.data`), the data pointed to is guaranteed to be '\\0'-terminated.

:sip:ref:`~PyQt6.QtCore.QByteArray` makes a deep copy of the ``const char \*`` data, so you can modify it later without experiencing side effects. (If, for example for performance reasons, you don't want to take a deep copy of the data, use QByteArray::fromRawData() instead.)

Another approach is to set the size of the array using :sip:ref:`~PyQt6.QtCore.QByteArray.resize` and to initialize the data byte by byte. :sip:ref:`~PyQt6.QtCore.QByteArray` uses 0-based indexes, just like C++ arrays. To access the byte at a particular index position, you can use operator[](). On non-const byte arrays, operator[]() returns a reference to a byte that can be used on the left side of an assignment. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 63-69

For read-only access, an alternative syntax is to use :sip:ref:`~PyQt6.QtCore.QByteArray.at`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 74-77

:sip:ref:`~PyQt6.QtCore.QByteArray.at` can be faster than operator[](), because it never causes a `deep copy <https://doc.qt.io/qt-6/implicit-sharing.html#deep-copy>`_ to occur.

To extract many bytes at a time, use :sip:ref:`~PyQt6.QtCore.QByteArray.first`, :sip:ref:`~PyQt6.QtCore.QByteArray.last`, or :sip:ref:`~PyQt6.QtCore.QByteArray.sliced`.

A :sip:ref:`~PyQt6.QtCore.QByteArray` can embed '\\0' bytes. The :sip:ref:`~PyQt6.QtCore.QByteArray.size` function always returns the size of the whole array, including embedded '\\0' bytes, but excluding the terminating '\\0' added by :sip:ref:`~PyQt6.QtCore.QByteArray`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 464-479

If you want to obtain the length of the data up to and excluding the first '\\0' byte, call qstrlen() on the byte array.

After a call to :sip:ref:`~PyQt6.QtCore.QByteArray.resize`, newly allocated bytes have undefined values. To set all the bytes to a particular value, call :sip:ref:`~PyQt6.QtCore.QByteArray.fill`.

To obtain a pointer to the actual bytes, call :sip:ref:`~PyQt6.QtCore.QByteArray.data` or constData(). These functions return a pointer to the beginning of the data. The pointer is guaranteed to remain valid until a non-const function is called on the :sip:ref:`~PyQt6.QtCore.QByteArray`. It is also guaranteed that the data ends with a '\\0' byte unless the :sip:ref:`~PyQt6.QtCore.QByteArray` was created from raw data. This '\\0' byte is automatically provided by :sip:ref:`~PyQt6.QtCore.QByteArray` and is not counted in :sip:ref:`~PyQt6.QtCore.QByteArray.size`.

:sip:ref:`~PyQt6.QtCore.QByteArray` provides the following basic functions for modifying the byte data: :sip:ref:`~PyQt6.QtCore.QByteArray.append`, :sip:ref:`~PyQt6.QtCore.QByteArray.prepend`, :sip:ref:`~PyQt6.QtCore.QByteArray.insert`, :sip:ref:`~PyQt6.QtCore.QByteArray.replace`, and :sip:ref:`~PyQt6.QtCore.QByteArray.remove`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 82-85

In the above example the :sip:ref:`~PyQt6.QtCore.QByteArray.replace` function's first two arguments are the position from which to start replacing and the number of bytes that should be replaced.

When data-modifying functions increase the size of the array, they may lead to reallocation of memory for the :sip:ref:`~PyQt6.QtCore.QByteArray` object. When this happens, :sip:ref:`~PyQt6.QtCore.QByteArray` expands by more than it immediately needs so as to have space for further expansion without reallocation until the size of the array has greatly increased.

The :sip:ref:`~PyQt6.QtCore.QByteArray.insert`, :sip:ref:`~PyQt6.QtCore.QByteArray.remove` and, when replacing a sub-array with one of different size, :sip:ref:`~PyQt6.QtCore.QByteArray.replace` functions can be slow (`linear time <https://doc.qt.io/qt-6/containers.html#linear-time>`_) for large arrays, because they require moving many bytes in the array by at least one position in memory.

If you are building a :sip:ref:`~PyQt6.QtCore.QByteArray` gradually and know in advance approximately how many bytes the :sip:ref:`~PyQt6.QtCore.QByteArray` will contain, you can call :sip:ref:`~PyQt6.QtCore.QByteArray.reserve`, asking :sip:ref:`~PyQt6.QtCore.QByteArray` to preallocate a certain amount of memory. You can also call :sip:ref:`~PyQt6.QtCore.QByteArray.capacity` to find out how much memory the :sip:ref:`~PyQt6.QtCore.QByteArray` actually has allocated.

Note that using non-const operators and functions can cause :sip:ref:`~PyQt6.QtCore.QByteArray` to do a deep copy of the data, due to `implicit sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_.

:sip:ref:`~PyQt6.QtCore.QByteArray` provides `STL-style iterators <https://doc.qt.io/qt-6/containers.html#stl-style-iterators>`_ (QByteArray::const_iterator and QByteArray::iterator). In practice, iterators are handy when working with generic algorithms provided by the C++ standard library.

**Note:** Iterators and references to individual :sip:ref:`~PyQt6.QtCore.QByteArray` elements are subject to stability issues. They are often invalidated when a :sip:ref:`~PyQt6.QtCore.QByteArray`-modifying operation (e.g. :sip:ref:`~PyQt6.QtCore.QByteArray.insert` or :sip:ref:`~PyQt6.QtCore.QByteArray.remove`) is called. When stability and iterator-like functionality is required, you should use indexes instead of iterators as they are not tied to :sip:ref:`~PyQt6.QtCore.QByteArray`'s internal state and thus do not get invalidated.

**Note:** Iterators over a :sip:ref:`~PyQt6.QtCore.QByteArray`, and references to individual bytes within one, cannot be relied on to remain valid when any non-const method of the :sip:ref:`~PyQt6.QtCore.QByteArray` is called. Accessing such an iterator or reference after the call to a non-const method leads to undefined behavior. When stability for iterator-like functionality is required, you should use indexes instead of iterators as they are not tied to :sip:ref:`~PyQt6.QtCore.QByteArray`'s internal state and thus do not get invalidated.

If you want to find all occurrences of a particular byte or sequence of bytes in a :sip:ref:`~PyQt6.QtCore.QByteArray`, use :sip:ref:`~PyQt6.QtCore.QByteArray.indexOf` or :sip:ref:`~PyQt6.QtCore.QByteArray.lastIndexOf`. The former searches forward starting from a given index position, the latter searches backward. Both return the index position of the byte sequence if they find it; otherwise, they return -1. For example, here's a typical loop that finds all occurrences of a particular string:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 90-95

If you simply want to check whether a :sip:ref:`~PyQt6.QtCore.QByteArray` contains a particular byte sequence, use :sip:ref:`~PyQt6.QtCore.QByteArray.contains`. If you want to find out how many times a particular byte sequence occurs in the byte array, use :sip:ref:`~PyQt6.QtCore.QByteArray.count`. If you want to replace all occurrences of a particular value with another, use one of the two-parameter :sip:ref:`~PyQt6.QtCore.QByteArray.replace` overloads.

:sip:ref:`~PyQt6.QtCore.QByteArray`\ s can be compared using overloaded operators such as operator<(), operator<=(), operator==(), operator>=(), and so on. The comparison is based exclusively on the numeric values of the bytes and is very fast, but is not what a human would expect. QString::localeAwareCompare() is a better choice for sorting user-interface strings.

For historical reasons, :sip:ref:`~PyQt6.QtCore.QByteArray` distinguishes between a null byte array and an empty byte array. A *null* byte array is a byte array that is initialized using :sip:ref:`~PyQt6.QtCore.QByteArray`'s default constructor or by passing (const char \*)0 to the constructor. An *empty* byte array is any byte array with size 0. A null byte array is always empty, but an empty byte array isn't necessarily null:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 100-107

All functions except :sip:ref:`~PyQt6.QtCore.QByteArray.isNull` treat null byte arrays the same as empty byte arrays. For example, :sip:ref:`~PyQt6.QtCore.QByteArray.data` returns a valid pointer (\ *not* nullptr) to a '\\0' byte for a null byte array and :sip:ref:`~PyQt6.QtCore.QByteArray` compares equal to :sip:ref:`~PyQt6.QtCore.QByteArray`\ (""). We recommend that you always use :sip:ref:`~PyQt6.QtCore.QByteArray.isEmpty` and avoid :sip:ref:`~PyQt6.QtCore.QByteArray.isNull`.

.. _qbytearray-maximum-size-and-out-of-memory-conditions:

Maximum size and out-of-memory conditions
-----------------------------------------

The maximum size of :sip:ref:`~PyQt6.QtCore.QByteArray` depends on the architecture. Most 64-bit systems can allocate more than 2 GB of memory, with a typical limit of 2^63 bytes. The actual value also depends on the overhead required for managing the data block. As a result, you can expect the maximum size of 2 GB minus overhead on 32-bit platforms, and 2^63 bytes minus overhead on 64-bit platforms. The number of elements that can be stored in a :sip:ref:`~PyQt6.QtCore.QByteArray` is this maximum size.

When memory allocation fails, :sip:ref:`~PyQt6.QtCore.QByteArray` throws a ``std::bad_alloc`` exception if the application is being compiled with exception support. Out of memory conditions in Qt containers are the only case where Qt will throw exceptions. If exceptions are disabled, then running out of memory is undefined behavior.

Note that the operating system may impose further limits on applications holding a lot of allocated memory, especially large, contiguous blocks. Such considerations, the configuration of such behavior or any mitigation are outside the scope of the :sip:ref:`~PyQt6.QtCore.QByteArray` API.

.. _qbytearray-c-locale-and-ascii-functions:

C locale and ASCII functions
----------------------------

:sip:ref:`~PyQt6.QtCore.QByteArray` generally handles data as bytes, without presuming any semantics; where it does presume semantics, it uses the C locale and ASCII encoding. Standard Unicode encodings are supported by QString, other encodings may be supported using :sip:ref:`~PyQt6.QtCore.QStringEncoder` and :sip:ref:`~PyQt6.QtCore.QStringDecoder` to convert to Unicode. For locale-specific interpretation of text, use :sip:ref:`~PyQt6.QtCore.QLocale` or QString.

.. _qbytearray-c-strings:

C Strings
.........

Traditional C strings, also known as '\\0'-terminated strings, are sequences of bytes, specified by a start-point and implicitly including each byte up to, but not including, the first '\\0' byte thereafter. Methods that accept such a pointer, without a length, will interpret it as this sequence of bytes. Such a sequence, by construction, cannot contain a '\\0' byte.

Other overloads accept a start-pointer and a byte-count; these use the given number of bytes, following the start address, regardless of whether any of them happen to be '\\0' bytes. In some cases, where there is no overload taking only a pointer, passing a length of -1 will cause the method to use the offset of the first '\\0' byte after the pointer as the length; a length of -1 should only be passed if the method explicitly says it does this (in which case it is typically a default argument).

.. _qbytearray-spacing-characters:

Spacing Characters
..................

A frequent requirement is to remove spacing characters from a byte array (``'\n'``, ``'\t'``, ``' '``, etc.). If you want to remove spacing from both ends of a :sip:ref:`~PyQt6.QtCore.QByteArray`, use :sip:ref:`~PyQt6.QtCore.QByteArray.trimmed`. If you want to also replace each run of spacing characters with a single space character within the byte array, use :sip:ref:`~PyQt6.QtCore.QByteArray.simplified`. Only ASCII spacing characters are recognized for these purposes.

.. _qbytearray-number-string-conversions:

Number-String Conversions
.........................

Functions that perform conversions between numeric data types and string representations are performed in the C locale, regardless of the user's locale settings. Use :sip:ref:`~PyQt6.QtCore.QLocale` to perform locale-aware conversions between numbers and strings.

.. _qbytearray-character-case:

Character Case
..............

In :sip:ref:`~PyQt6.QtCore.QByteArray`, the notion of uppercase and lowercase and of case-independent comparison is limited to ASCII. Non-ASCII characters are treated as caseless, since their case depends on encoding. This affects functions that support a case insensitive option or that change the case of their arguments. Functions that this affects include :sip:ref:`~PyQt6.QtCore.QByteArray.contains`, :sip:ref:`~PyQt6.QtCore.QByteArray.indexOf`, :sip:ref:`~PyQt6.QtCore.QByteArray.lastIndexOf`, :sip:ref:`~PyQt6.QtCore.QByteArray.isLower`, :sip:ref:`~PyQt6.QtCore.QByteArray.isUpper`, :sip:ref:`~PyQt6.QtCore.QByteArray.toLower` and :sip:ref:`~PyQt6.QtCore.QByteArray.toUpper`.

This issue does not apply to QStrings since they represent characters using Unicode.

.. seealso:: QByteArrayView, QString, :sip:ref:`~PyQt6.QtCore.QBitArray`.
