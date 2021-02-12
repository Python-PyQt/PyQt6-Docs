.. sip:class-description::
    :status: todo
    :brief: QByteArray::FromBase64Result class holds the result of a call to QByteArray::fromBase64Encoding
    :digest: f31fedec9975a24a749b7d4f7adb0780

The :sip:ref:`~PyQt6.QtCore.QByteArray.FromBase64Result` class holds the result of a call to :sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64Encoding`.

Objects of this class can be used to check whether the conversion was successful, and if so, retrieve the decoded :sip:ref:`~PyQt6.QtCore.QByteArray`. The conversion operators defined for :sip:ref:`~PyQt6.QtCore.QByteArray.FromBase64Result` make its usage straightforward:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 430-433

Alternatively, it is possible to access the conversion status and the decoded data directly:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 437-439

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64`.
