.. sip:method-description::
    :status: todo
    :pysig: e2c4218bd14a725819f91a09a6314bd5
    :realsig: (QEvent::Type, int, Qt::KeyboardModifiers, quint32, quint32, quint32, const QString&, bool, quint16, const QInputDevice*)
    :digest: 5c5f4546df3c705a39082b522247424a

Constructs a key event object.

The *type* parameter must be :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyPress`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyRelease`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.ShortcutOverride`.

Int *key* is the code for the :sip:ref:`~PyQt6.QtCore.Qt.Key` that the event loop should listen for. If *key* is 0, the event is not a result of a known key; for example, it may be the result of a compose sequence or keyboard macro. The *modifiers* holds the keyboard modifiers, and the given *text* is the Unicode text that the key generated. If *autorep* is true, :sip:ref:`~PyQt6.QtGui.QKeyEvent.isAutoRepeat` will be true. *count* is the number of keys involved in the event.

In addition to the normal key event data, also contains *nativeScanCode*, *nativeVirtualKey* and *nativeModifiers*. This extra data is used by the shortcut system, to determine which shortcuts to trigger.
