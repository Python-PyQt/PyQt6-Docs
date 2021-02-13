.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2abd376892138a435b2ca7d61302b1c1

Returns ``true`` if the socket is encrypted; otherwise, false is returned.

An encrypted socket encrypts all data that is written by calling write() or putChar() before the data is written to the network, and decrypts all incoming data as the data is received from the network, before you call read(), readLine() or getChar().

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` when it enters encrypted mode.

You can call :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sessionCipher` to find which cryptographic cipher is used to encrypt and decrypt your data.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.mode`.
