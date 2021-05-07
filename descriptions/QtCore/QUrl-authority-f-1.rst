.. sip:method-description::
    :status: todo
    :pysig: bab5c0e581d25682638382ee3c1c852b
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: f9802feee26c0a9d90a2c0598c9a1921

Returns the authority of the URL if it is defined; otherwise an empty string is returned.

This function returns an unambiguous value, which may contain that characters still percent-encoded, plus some control sequences not representable in decoded form in QString.

The *options* argument controls how to format the user info component. The value of :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded` is not permitted in this function. If you need to obtain fully decoded data, call :sip:ref:`~PyQt6.QtCore.QUrl.userName`, :sip:ref:`~PyQt6.QtCore.QUrl.password`, :sip:ref:`~PyQt6.QtCore.QUrl.host` and :sip:ref:`~PyQt6.QtCore.QUrl.port` individually.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setAuthority`, :sip:ref:`~PyQt6.QtCore.QUrl.userInfo`, :sip:ref:`~PyQt6.QtCore.QUrl.userName`, :sip:ref:`~PyQt6.QtCore.QUrl.password`, :sip:ref:`~PyQt6.QtCore.QUrl.host`, :sip:ref:`~PyQt6.QtCore.QUrl.port`.
