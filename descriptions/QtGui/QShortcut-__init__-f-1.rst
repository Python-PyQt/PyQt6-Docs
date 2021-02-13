.. sip:method-description::
    :status: todo
    :pysig: 841335a09d6dbe713a2ecb15f3b41748
    :realsig: (QKeySequence::StandardKey,QObject*,const char*,const char*,Qt::ShortcutContext)
    :digest: 6913339bc995e8adb0db475a4311a6e4

Constructs a :sip:ref:`~PyQt6.QtGui.QShortcut` object for the *parent*, which should be a :sip:ref:`~PyQt6.QtGui.QWindow` or a QWidget.

The shortcut operates on its parent, listening for :sip:ref:`~PyQt6.QtGui.QShortcutEvent`\ s that match the *standardKey*. Depending on the ambiguity of the event, the shortcut will call the *member* function, or the *ambiguousMember* function, if the key press was in the shortcut's *context*.
