.. sip:method-description::
    :status: todo
    :pysig: 841335a09d6dbe713a2ecb15f3b41748
    :realsig: (QKeySequence::StandardKey,QObject*,const char*,const char*,Qt::ShortcutContext)
    :digest: 92daf86828de2d131ec7f44d0a2edfb3

Constructs a :sip:ref:`~PyQt6.QtGui.QShortcut` object for the *parent*, which should be a :sip:ref:`~PyQt6.QtGui.QWindow` or a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_.

The shortcut operates on its parent, listening for :sip:ref:`~PyQt6.QtGui.QShortcutEvent`\ s that match the *standardKey*. Depending on the ambiguity of the event, the shortcut will call the *member* function, or the *ambiguousMember* function, if the key press was in the shortcut's *context*.
