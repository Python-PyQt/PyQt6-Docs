.. sip:class-description::
    :status: todo
    :brief: State-based decoder for text
    :digest: 63f748705e99e4306606339cb6d9bc26

The :sip:ref:`~PyQt6.QtCore.QStringDecoder` class provides a state-based decoder for text.

A text decoder converts text an encoded text format that uses a specific encoding into Qt's internal representation.

Converting encoded data into a QString can be achieved using the following code:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qstringconverter.py
    :lines: 54-56

The decoder remembers any state that is required between calls, so converting data received in chunks, for example, when receiving it over a network, is just as easy, by calling the decoder whenever new data is available:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qstringconverter.py
    :lines: 68-74

The :sip:ref:`~PyQt6.QtCore.QStringDecoder` object maintains state between chunks and therefore works correctly even if chunks are split in the middle of a multi-byte character sequence.

:sip:ref:`~PyQt6.QtCore.QStringDecoder` objects can't be copied because of their internal state, but can be moved.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStringConverter`, :sip:ref:`~PyQt6.QtCore.QStringEncoder`.
