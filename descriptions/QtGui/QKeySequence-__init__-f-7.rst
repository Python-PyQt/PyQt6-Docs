.. sip:method-description::
    :status: todo
    :pysig: 4cea57770bfe0e23917154e4dc906951
    :realsig: (const QString&, QKeySequence::SequenceFormat)
    :digest: f257bb3ff09f34a13296682d331ce852

Creates a key sequence from the *key* string, based on *format*.

For example "Ctrl+O" gives CTRL+'O'. The strings "Ctrl", "Shift", "Alt" and "Meta" are recognized, as well as their translated equivalents in the "\ :sip:ref:`~PyQt6.QtGui.QShortcut`" context (using :sip:ref:`~PyQt6.QtCore.QObject.tr`).

Up to four key codes may be entered by separating them with commas, e.g. "Alt+X,Ctrl+S,Q".

This constructor is typically used with :sip:ref:`~PyQt6.QtCore.QObject.tr`\ (), so that shortcut keys can be replaced in translations:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qkeysequence.py
    :lines: 82-84

Note the "File|Open" translator comment. It is by no means necessary, but it provides some context for the human translator.
