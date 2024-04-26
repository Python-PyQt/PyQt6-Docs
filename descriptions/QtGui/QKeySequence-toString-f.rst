.. sip:method-description::
    :status: todo
    :pysig: a5a34e1275955830c803a59b0290a183
    :realsig: (QKeySequence::SequenceFormat) const
    :digest: 1e3e91221d3ed393513144ad7f04f8ec

Return a string representation of the key sequence, based on *format*.

For example, the value :sip:ref:`~PyQt6.QtCore.Qt.Modifier.CTRL`+\ :sip:ref:`~PyQt6.QtCore.Qt.Key.Key_O` results in "Ctrl+O". If the key sequence has multiple key codes, each is separated by commas in the string returned, such as "Alt+X, Ctrl+Y, Z". The strings, "Ctrl", "Shift", etc. are translated using :sip:ref:`~PyQt6.QtCore.QObject.tr` in the "\ :sip:ref:`~PyQt6.QtGui.QShortcut`" context.

If the key sequence has no keys, an empty string is returned.

On Apple platforms, the string returned resembles the sequence that is shown in the menu bar if *format* is :sip:ref:`~PyQt6.QtGui.QKeySequence.SequenceFormat.NativeText`; otherwise, the string uses the "portable" format, suitable for writing to a file.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QKeySequence.fromString`.
