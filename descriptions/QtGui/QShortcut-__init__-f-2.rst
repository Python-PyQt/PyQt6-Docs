.. sip:method-description::
    :status: todo
    :pysig: b9ea41c3abee5343855e3a4c70bde2f5
    :realsig: (const QKeySequence&,QObject*,const char*,const char*,Qt::ShortcutContext)
    :digest: ed9a3baa03a22f313e480f582434672f

Constructs a :sip:ref:`~PyQt6.QtGui.QShortcut` object for the *parent*, which should be a :sip:ref:`~PyQt6.QtGui.QWindow` or a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_.

The shortcut operates on its parent, listening for :sip:ref:`~PyQt6.QtGui.QShortcutEvent`\ s that match the *key* sequence. Depending on the ambiguity of the event, the shortcut will call the *member* function, or the *ambiguousMember* function, if the key press was in the shortcut's *context*.
