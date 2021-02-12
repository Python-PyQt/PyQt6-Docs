.. sip:class-description::
    :status: todo
    :brief: Way to generate hash-based message authentication codes
    :digest: ac00b864efced02ae2e9e61652d27b46

The :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode` class provides a way to generate hash-based message authentication codes.

:sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode` supports all cryptographic hashes which are supported by :sip:ref:`~PyQt6.QtCore.QCryptographicHash`.

To generate message authentication code, pass hash algorithm :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm` to constructor, then set key and message by :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.setKey` and :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.addData` functions. Result can be acquired by :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.result` function.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qmessageauthenticationcode-main.py
    :lines: 60-61

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qmessageauthenticationcode-main.py
    :lines: 65-68

Alternatively, this effect can be achieved by providing message, key and method to :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.hash` method.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qmessageauthenticationcode-main.py
    :lines: 72-72

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCryptographicHash`.
