.. sip:class-description::
    :status: todo
    :brief: State-based encoder for text
    :digest: 2eb4f79ba303640b3337808d7ed8d3f9

The :sip:ref:`~PyQt6.QtCore.QStringEncoder` class provides a state-based encoder for text.

A text encoder converts text from Qt's internal representation into an encoded text format using a specific encoding.

Converting a string from Unicode to the local encoding can be achieved using the following code:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qstringconverter.py
    :lines: 61-63

The encoder remembers any state that is required between calls, so converting data received in chunks, for example, when receiving it over a network, is just as easy, by calling the encoder whenever new data is available:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qstringconverter.py
    :lines: 78-84

The :sip:ref:`~PyQt6.QtCore.QStringEncoder` object maintains state between chunks and therefore works correctly even if a UTF-16 surrogate character is split between chunks.

:sip:ref:`~PyQt6.QtCore.QStringEncoder` objects can't be copied because of their internal state, but can be moved.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStringConverter`, :sip:ref:`~PyQt6.QtCore.QStringDecoder`.
