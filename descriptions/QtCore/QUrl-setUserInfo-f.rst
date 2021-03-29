.. sip:method-description::
    :status: todo
    :pysig: a22ebaa09d7b4d7f39256027764f9bab
    :realsig: (const QString&,QUrl::ParsingMode)
    :digest: 878fc2b9bf82dafe7df58629adc0d4b1

Sets the user info of the URL to *userInfo*. The user info is an optional part of the authority of the URL, as described in :sip:ref:`~PyQt6.QtCore.QUrl.setAuthority`.

The user info consists of a user name and optionally a password, separated by a ':'. If the password is empty, the colon must be omitted. The following example shows a valid user info string:

.. image:: ../../../images/qurl-authority3.png

The *userInfo* data is interpreted according to *mode*: in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, any '%' characters must be followed by exactly two hexadecimal characters and some characters (including space) are not allowed in undecoded form. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode` (the default), all characters are accepted in undecoded form and the tolerant parser will correct stray '%' not followed by two hex characters.

This function does not allow *mode* to be :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode`. To set fully decoded data, call :sip:ref:`~PyQt6.QtCore.QUrl.setUserName` and :sip:ref:`~PyQt6.QtCore.QUrl.setPassword` individually.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.userInfo`, :sip:ref:`~PyQt6.QtCore.QUrl.setUserName`, :sip:ref:`~PyQt6.QtCore.QUrl.setPassword`, :sip:ref:`~PyQt6.QtCore.QUrl.setAuthority`.
