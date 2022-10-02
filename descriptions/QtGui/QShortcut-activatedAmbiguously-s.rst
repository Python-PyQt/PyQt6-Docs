.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0a25d9d052dcdce52401a1b8d028cbff

When a key sequence is being typed at the keyboard, it is said to be ambiguous as long as it matches the start of more than one shortcut.

When a shortcut's key sequence is completed, activatedAmbiguously() is emitted if the key sequence is still ambiguous (i.e., it is the start of one or more other shortcuts). The :sip:ref:`~PyQt6.QtGui.QShortcut.activated` signal is not emitted in this case.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QShortcut.activated`.
