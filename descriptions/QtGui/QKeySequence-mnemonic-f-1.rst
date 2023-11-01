.. sip:method-description::
    :status: todo
    :pysig: 2280d69e592fbd7cb25be42b34c0d7da
    :realsig: (const QString&)
    :digest: 2f1904270be2dd596db429d8e101bdea

Returns the shortcut key sequence for the mnemonic in *text*, or an empty key sequence if no mnemonics are found.

For example, mnemonic("E&xit") returns ``Qt::ALT+Qt::Key_X``, mnemonic("&Quit") returns ``ALT+Key_Q``, and mnemonic("Quit") returns an empty :sip:ref:`~PyQt6.QtGui.QKeySequence`.
