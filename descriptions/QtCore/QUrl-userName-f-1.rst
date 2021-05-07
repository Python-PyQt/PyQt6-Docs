.. sip:method-description::
    :status: todo
    :pysig: 95c5a62151d056a62c97d208f5476f2a
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: 9da8bc25164d6e73689c61f78f095044

Returns the user name of the URL if it is defined; otherwise an empty string is returned.

The *options* argument controls how to format the user name component. All values produce an unambiguous result. With :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded`, all percent-encoded sequences are decoded; otherwise, the returned value may contain some percent-encoded sequences for some control sequences not representable in decoded form in QString.

Note that :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded` may cause data loss if those non-representable sequences are present. It is recommended to use that value when the result will be used in a non-URL context, such as setting in :sip:ref:`~PyQt6.QtNetwork.QAuthenticator` or negotiating a login.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setUserName`, :sip:ref:`~PyQt6.QtCore.QUrl.userInfo`.
