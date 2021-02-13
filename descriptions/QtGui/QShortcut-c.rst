.. sip:class-description::
    :status: todo
    :brief: Used to create keyboard shortcuts
    :digest: 9017a83aa2d6017bd8d5d36721d7afa9

The :sip:ref:`~PyQt6.QtGui.QShortcut` class is used to create keyboard shortcuts.

The :sip:ref:`~PyQt6.QtGui.QShortcut` class provides a way of connecting keyboard shortcuts to Qt's `signals and slots <https://doc.qt.io/qt-6/signalsandslots.html>`_ mechanism, so that objects can be informed when a shortcut is executed. The shortcut can be set up to contain all the key presses necessary to describe a keyboard shortcut, including the states of modifier keys such as Shift, Ctrl, and Alt.

.. _qshortcut-mnemonic:

In widget applications, certain widgets can use '&' in front of a character. This will automatically create a mnemonic (a shortcut) for that character, e.g. "E&xit" will create the shortcut Alt+X (use '&&' to display an actual ampersand). The widget might consume and perform an action on a given shortcut. On X11 the ampersand will not be shown and the character will be underlined. On Windows, shortcuts are normally not displayed until the user presses the Alt key, but this is a setting the user can change. On Mac, shortcuts are disabled by default. Call :sip:ref:`~PyQt6.QtGui.qt_set_sequence_auto_mnemonic` to enable them. However, because mnemonic shortcuts do not fit in with Aqua's guidelines, Qt will not show the shortcut character underlined.

For applications that use menus, it may be more convenient to use the convenience functions provided in the QMenu class to assign keyboard shortcuts to menu items as they are created. Alternatively, shortcuts may be associated with other types of actions in the :sip:ref:`~PyQt6.QtGui.QAction` class.

The simplest way to create a shortcut for a particular widget is to construct the shortcut with a key sequence. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qshortcut.py
    :lines: 54-55

When the user types the :sip:ref:`~PyQt6.QtGui.QKeySequence` for a given shortcut, the shortcut's :sip:ref:`~PyQt6.QtGui.QShortcut.activated` signal is emitted. (In the case of ambiguity, the :sip:ref:`~PyQt6.QtGui.QShortcut.activatedAmbiguously` signal is emitted.) A shortcut is "listened for" by Qt's event loop when the shortcut's parent widget is receiving events.

A shortcut's key sequence can be set with :sip:ref:`~PyQt6.QtGui.QShortcut.setKey` and retrieved with :sip:ref:`~PyQt6.QtGui.QShortcut.key`. A shortcut can be enabled or disabled with :sip:ref:`~PyQt6.QtGui.QShortcut.setEnabled`, and can have "What's This?" help text set with :sip:ref:`~PyQt6.QtGui.QShortcut.setWhatsThis`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QShortcutEvent`, :sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QAction`.
