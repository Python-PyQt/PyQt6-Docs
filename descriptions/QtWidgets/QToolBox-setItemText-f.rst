.. sip:method-description::
    :status: todo
    :pysig: d4d85079d3c184e4c59bdc73add11325
    :realsig: (int,const QString&)
    :digest: a303d354529ca3be80ef76486f48bb89

Sets the text of the item at position *index* to *text*.

If the provided text contains an ampersand character ('&'), a mnemonic is automatically created for it. The character that follows the '&' will be used as the shortcut key. Any previous mnemonic will be overwritten, or cleared if no mnemonic is defined by the text. See the QShortcut documentation for details (to display an actual ampersand, use '&&').

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QToolBox.itemText`.
