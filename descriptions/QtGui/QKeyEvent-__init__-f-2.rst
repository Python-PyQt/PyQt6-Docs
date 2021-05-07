.. sip:method-description::
    :status: todo
    :pysig: e0dbd1a98727881b1a72c064d164ffdc
    :realsig: (QEvent::Type,int,Qt::KeyboardModifiers,const QString&,bool,quint16)
    :digest: e23b83417143f4b973c7a1f54eaad600

Constructs a key event object.

The *type* parameter must be :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyPress`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyRelease`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.ShortcutOverride`.

Int *key* is the code for the :sip:ref:`~PyQt6.QtCore.Qt.Key` that the event loop should listen for. If *key* is 0, the event is not a result of a known key; for example, it may be the result of a compose sequence or keyboard macro. The *modifiers* holds the keyboard modifiers, and the given *text* is the Unicode text that the key generated. If *autorep* is true, :sip:ref:`~PyQt6.QtGui.QKeyEvent.isAutoRepeat` will be true. *count* is the number of keys involved in the event.
