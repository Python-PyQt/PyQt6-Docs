.. sip:method-description::
    :status: todo
    :pysig: ee0b42ff8884951c9f452d6c23ec55ea
    :realsig: (QKeySequence::StandardKey,QObject*,const char*,const char*,Qt::ShortcutContext)
    :digest: 92daf86828de2d131ec7f44d0a2edfb3

Constructs a :sip:ref:`~PyQt6.QtGui.QShortcut` object for the *parent*, which should be a :sip:ref:`~PyQt6.QtGui.QWindow` or a :sip:ref:`~PyQt6.QtWidgets.QWidget`.

The shortcut operates on its parent, listening for :sip:ref:`~PyQt6.QtGui.QShortcutEvent`\ s that match the *standardKey*. Depending on the ambiguity of the event, the shortcut will call the *member* function, or the *ambiguousMember* function, if the key press was in the shortcut's *context*.
