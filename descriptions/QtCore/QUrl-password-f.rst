.. sip:method-description::
    :status: todo
    :pysig: 75b41bd8a3b4bb4aa098c1a485c252d8
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: a8b2ca4d4f9e997770381f7a1be93218

Returns the password of the URL if it is defined; otherwise an empty string is returned.

The *options* argument controls how to format the user name component. All values produce an unambiguous result. With :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded`, all percent-encoded sequences are decoded; otherwise, the returned value may contain some percent-encoded sequences for some control sequences not representable in decoded form in QString.

Note that :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` may cause data loss if those non-representable sequences are present. It is recommended to use that value when the result will be used in a non-URL context, such as setting in QAuthenticator or negotiating a login.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setPassword`.
