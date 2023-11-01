.. sip:method-description::
    :status: todo
    :pysig: 68e9f7176d2fd3d9da14bf66cc218b40
    :realsig: (const QString&, QUrl::ParsingMode)
    :digest: 0e7c4917867ffdea0dc31838aa456ff0

Sets the authority of the URL to *authority*.

The authority of a URL is the combination of user info, a host name and a port. All of these elements are optional; an empty authority is therefore valid.

The user info and host are separated by a '@', and the host and port are separated by a ':'. If the user info is empty, the '@' must be omitted; although a stray ':' is permitted if the port is empty.

The following example shows a valid authority string:

.. image:: ../../../images/qurl-authority.png

The *authority* data is interpreted according to *mode*: in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, any '%' characters must be followed by exactly two hexadecimal characters and some characters (including space) are not allowed in undecoded form. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode` (the default), all characters are accepted in undecoded form and the tolerant parser will correct stray '%' not followed by two hex characters.

This function does not allow *mode* to be :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode`. To set fully decoded data, call :sip:ref:`~PyQt6.QtCore.QUrl.setUserName`, :sip:ref:`~PyQt6.QtCore.QUrl.setPassword`, :sip:ref:`~PyQt6.QtCore.QUrl.setHost` and :sip:ref:`~PyQt6.QtCore.QUrl.setPort` individually.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.authority`, :sip:ref:`~PyQt6.QtCore.QUrl.setUserInfo`, :sip:ref:`~PyQt6.QtCore.QUrl.setHost`, :sip:ref:`~PyQt6.QtCore.QUrl.setPort`.
