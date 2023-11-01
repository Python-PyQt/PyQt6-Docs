.. sip:method-description::
    :status: todo
    :pysig: b0676b48f29a91e45b70bd9474938365
    :realsig: (const QKeySequence&, QObject*, const char*, const char*, Qt::ShortcutContext)
    :digest: ed9a3baa03a22f313e480f582434672f

Constructs a :sip:ref:`~PyQt6.QtGui.QShortcut` object for the *parent*, which should be a :sip:ref:`~PyQt6.QtGui.QWindow` or a :sip:ref:`~PyQt6.QtWidgets.QWidget`.

The shortcut operates on its parent, listening for :sip:ref:`~PyQt6.QtGui.QShortcutEvent`\ s that match the *key* sequence. Depending on the ambiguity of the event, the shortcut will call the *member* function, or the *ambiguousMember* function, if the key press was in the shortcut's *context*.
