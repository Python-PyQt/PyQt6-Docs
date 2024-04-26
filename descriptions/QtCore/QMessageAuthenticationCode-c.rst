.. sip:class-description::
    :status: todo
    :brief: Way to generate hash-based message authentication codes
    :digest: 19bf41e5b8648b748a60c80962830a97

The :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode` class provides a way to generate hash-based message authentication codes.

Use the :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode` class to generate hash-based message authentication codes (HMACs). The class supports all cryptographic hash algorithms from :sip:ref:`~PyQt6.QtCore.QCryptographicHash` (see also :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm`).

To generate a message authentication code, pass a suitable hash algorithm and secret key to the constructor. Then process the message data by calling :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.addData` one or more times. After the full message has been processed, get the final authentication code via the :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.result` function:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qmessageauthenticationcode-main.py
    :lines: 60-61

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qmessageauthenticationcode-main.py
    :lines: 65-68

For simple cases like above, you can also use the static :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.hash` function:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qmessageauthenticationcode-main.py
    :lines: 72-72

**Note:** The cryptographic strength of the HMAC depends upon the size of the secret key, and the security of the underlying hash function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCryptographicHash`, :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm`.
