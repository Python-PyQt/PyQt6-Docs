.. sip:class-description::
    :status: todo
    :brief: Array of bits
    :digest: ea86eb83b26f1585c3cdb2f9c01949b8

The :sip:ref:`~PyQt6.QtCore.QBitArray` class provides an array of bits.

A :sip:ref:`~PyQt6.QtCore.QBitArray` is an array that gives access to individual bits and provides operators (AND, OR, XOR, and NOT) that work on entire arrays of bits. It uses `implicit sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_ (copy-on-write) to reduce memory usage and to avoid the needless copying of data.

The following code constructs a :sip:ref:`~PyQt6.QtCore.QBitArray` containing 200 bits initialized to false (0):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 54-54

To initialize the bits to true, either pass ``true`` as second argument to the constructor, or call :sip:ref:`~PyQt6.QtCore.QBitArray.fill` later on.

:sip:ref:`~PyQt6.QtCore.QBitArray` uses 0-based indexes, just like C++ arrays. To access the bit at a particular index position, you can use operator[](). On non-const bit arrays, operator[]() returns a reference to a bit that can be used on the left side of an assignment. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 59-63

For technical reasons, it is more efficient to use :sip:ref:`~PyQt6.QtCore.QBitArray.testBit` and :sip:ref:`~PyQt6.QtCore.QBitArray.setBit` to access bits in the array than operator[](). For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 68-71

:sip:ref:`~PyQt6.QtCore.QBitArray` supports ``&`` (AND), ``|`` (OR), ``^`` (XOR), ``~`` (NOT), as well as ``&=``, ``|=``, and ``^=``. These operators work in the same way as the built-in C++ bitwise operators of the same name. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 76-85

For historical reasons, :sip:ref:`~PyQt6.QtCore.QBitArray` distinguishes between a null bit array and an empty bit array. A *null* bit array is a bit array that is initialized using :sip:ref:`~PyQt6.QtCore.QBitArray`'s default constructor. An *empty* bit array is any bit array with size 0. A null bit array is always empty, but an empty bit array isn't necessarily null:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qbitarray.py
    :lines: 90-97

All functions except :sip:ref:`~PyQt6.QtCore.QBitArray.isNull` treat null bit arrays the same as empty bit arrays; for example, :sip:ref:`~PyQt6.QtCore.QBitArray` compares equal to :sip:ref:`~PyQt6.QtCore.QBitArray`\ (0). We recommend that you always use :sip:ref:`~PyQt6.QtCore.QBitArray.isEmpty` and avoid :sip:ref:`~PyQt6.QtCore.QBitArray.isNull`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray`, QList.
