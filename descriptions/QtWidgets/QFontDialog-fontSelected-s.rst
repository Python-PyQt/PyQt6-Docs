.. sip:signal-description::
    :status: todo
    :pysig: 59d522e2b645f1f78264c495a0d39146
    :realsig: (const QFont&)
    :digest: f7a0d62cfb06534d9557256cc09a0260

This signal is emitted when a font has been selected. The selected font is specified in *font*.

The signal is only emitted when a user has chosen the final font to be used. It is not emitted while the user is changing the current font in the font dialog.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFontDialog.selectedFont`, :sip:ref:`~PyQt6.QtWidgets.QFontDialog.currentFontChanged`, :sip:ref:`~PyQt6.QtWidgets.QFontDialog.currentFont`.
