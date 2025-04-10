.. sip:class-description::
    :status: todo
    :brief: Encapsulates a key sequence as used by shortcuts
    :digest: d14f793d46062616e2bd6eb4643b7993

The :sip:ref:`~PyQt6.QtGui.QKeySequence` class encapsulates a key sequence as used by shortcuts.

In its most common form, a key sequence describes a combination of keys that must be used together to perform some action. Key sequences are used with :sip:ref:`~PyQt6.QtGui.QAction` objects to specify which keyboard shortcuts can be used to trigger actions.

Key sequences can be constructed for use as keyboard shortcuts in three different ways:

* For standard shortcuts, a :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey` can be used to request the platform-specific key sequence associated with each shortcut.

* For custom shortcuts, human-readable strings such as "Ctrl+X" can be used, and these can be translated into the appropriate shortcuts for users of different languages. Translations are made in the "\ :sip:ref:`~PyQt6.QtGui.QShortcut`" context.

* For hard-coded shortcuts, integer key codes can be specified with a combination of values defined by the :sip:ref:`~PyQt6.QtCore.Qt.Key` and :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier` enum values. Each key code consists of a single :sip:ref:`~PyQt6.QtCore.Qt.Key` value and zero or more modifiers, such as :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.ShiftModifier`, :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.ControlModifier`, :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.AltModifier` and :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.MetaModifier`.

For example, Ctrl P might be a sequence used as a shortcut for printing a document, and can be specified in any of the following ways:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qkeysequence.py
    :lines: 64-68

Note that, for letters, the case used in the specification string does not matter. In the above examples, the user does not need to hold down the Shift key to activate a shortcut specified with "Ctrl+P". However, for other keys, the use of Shift as an unspecified extra modifier key can lead to confusion for users of an application whose keyboards have different layouts to those used by the developers. See the :ref:`qkeysequence-keyboard-layout-issues` section below for more details.

It is preferable to use standard shortcuts where possible. When creating key sequences for non-standard shortcuts, you should use human-readable strings in preference to hard-coded integer values.

:sip:ref:`~PyQt6.QtGui.QKeySequence` object can be serialized to human-readable strings with the :sip:ref:`~PyQt6.QtGui.QKeySequence.toString` function.

An alternative way to specify hard-coded key codes is to use the Unicode code point of the character; for example, 'A' gives the same key sequence as :sip:ref:`~PyQt6.QtCore.Qt.Key.Key_A`.

**Note:** On Apple platforms, references to "Ctrl", :sip:ref:`~PyQt6.QtCore.Qt.Modifier.CTRL`, :sip:ref:`~PyQt6.QtCore.Qt.Key.Key_Control` and :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.ControlModifier` correspond to the Command keys on the Macintosh keyboard, and references to "Meta", :sip:ref:`~PyQt6.QtCore.Qt.Modifier.META`, :sip:ref:`~PyQt6.QtCore.Qt.Key.Key_Meta` and :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.MetaModifier` correspond to the Control keys. In effect, developers can use the same shortcut descriptions across all platforms, and their applications will automatically work as expected on Apple platforms.

.. _qkeysequence-standard-shortcuts:

Standard Shortcuts
------------------

:sip:ref:`~PyQt6.QtGui.QKeySequence` defines many :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey` to reduce the amount of effort required when setting up actions in a typical application. The table below shows some common key sequences that are often used for these standard shortcuts by applications on four widely-used platforms. Note that on Apple platforms, the Ctrl value corresponds to the Command keys on the Macintosh keyboard, and the Meta value corresponds to the Control keys.

+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.StandardKey`              | Windows                                   | Apple platforms                                    | KDE Plasma                        | GNOME                  |
+===========================================================================+===========================================+====================================================+===================================+========================+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.HelpContents`             | F1                                        | Ctrl+?                                             | F1                                | F1                     |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.WhatsThis`                | Shift+F1                                  | Shift+F1                                           | Shift+F1                          | Shift+F1               |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Open                                                                      | Ctrl+O                                    | Ctrl+O                                             | Ctrl+O                            | Ctrl+O                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Close                                                                     | Ctrl+F4, Ctrl+W                           | Ctrl+W, Ctrl+F4                                    | Ctrl+W                            | Ctrl+W                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Save                                                                      | Ctrl+S                                    | Ctrl+S                                             | Ctrl+S                            | Ctrl+S                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Quit                                                                      |                                           | Ctrl+Q                                             | Ctrl+Q                            | Ctrl+Q                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SaveAs`                   | Ctrl+Shift+S                              | Ctrl+Shift+S                                       | Ctrl+Shift+S                      | Ctrl+Shift+S           |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| New                                                                       | Ctrl+N                                    | Ctrl+N                                             | Ctrl+N                            | Ctrl+N                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Delete                                                                    | Del                                       | Forward Delete, Meta+D                             | Del, Ctrl+D                       | Del, Ctrl+D            |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Cut                                                                       | Ctrl+X, Shift+Del                         | Ctrl+X, Meta+K                                     | Ctrl+X, F20, Shift+Del            | Ctrl+X, F20, Shift+Del |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Copy                                                                      | Ctrl+C, Ctrl+Ins                          | Ctrl+C                                             | Ctrl+C, F16, Ctrl+Ins             | Ctrl+C, F16, Ctrl+Ins  |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Paste                                                                     | Ctrl+V, Shift+Ins                         | Ctrl+V, Meta+Y                                     | Ctrl+V, F18, Shift+Ins            | Ctrl+V, F18, Shift+Ins |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Preferences                                                               |                                           | Ctrl+,                                             | Ctrl+Shift+,                      |                        |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Undo                                                                      | Ctrl+Z, Alt+Backspace                     | Ctrl+Z                                             | Ctrl+Z, F14                       | Ctrl+Z, F14            |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Redo                                                                      | Ctrl+Y, Shift+Ctrl+Z, Alt+Shift+Backspace | Ctrl+Shift+Z                                       | Ctrl+Shift+Z                      | Ctrl+Shift+Z           |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Back                                                                      | Alt+Left, Backspace                       | Ctrl+[                                             | Alt+Left                          | Alt+Left               |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Forward                                                                   | Alt+Right, Shift+Backspace                | Ctrl+]                                             | Alt+Right                         | Alt+Right              |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Refresh                                                                   | F5                                        | F5                                                 | F5                                | Ctrl+R, F5             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.ZoomIn`                   | Ctrl+Plus                                 | Ctrl+Plus                                          | Ctrl+Plus                         | Ctrl+Plus              |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.ZoomOut`                  | Ctrl+Minus                                | Ctrl+Minus                                         | Ctrl+Minus                        | Ctrl+Minus             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.FullScreen`               | F11, Alt+Enter                            | Ctrl+Meta+F                                        | F11, Ctrl+Shift+F                 | Ctrl+F11               |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Print                                                                     | Ctrl+P                                    | Ctrl+P                                             | Ctrl+P                            | Ctrl+P                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.AddTab`                   | Ctrl+T                                    | Ctrl+T                                             | Ctrl+Shift+N, Ctrl+T              | Ctrl+T                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.NextChild`                | Ctrl+Tab, Forward, Ctrl+F6                | Ctrl+}, Forward, Ctrl+Tab                          | Ctrl+Tab, Forward, Ctrl+Comma     | Ctrl+Tab, Forward      |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.PreviousChild`            | Ctrl+Shift+Tab, Back, Ctrl+Shift+F6       | Ctrl+{, Back, Ctrl+Shift+Tab                       | Ctrl+Shift+Tab, Back, Ctrl+Period | Ctrl+Shift+Tab, Back   |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Find                                                                      | Ctrl+F                                    | Ctrl+F                                             | Ctrl+F                            | Ctrl+F                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.FindNext`                 | F3, Ctrl+G                                | Ctrl+G                                             | F3                                | Ctrl+G, F3             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.FindPrevious`             | Shift+F3, Ctrl+Shift+G                    | Ctrl+Shift+G                                       | Shift+F3                          | Ctrl+Shift+G, Shift+F3 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Replace                                                                   | Ctrl+H                                    | (none)                                             | Ctrl+R                            | Ctrl+H                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectAll`                | Ctrl+A                                    | Ctrl+A                                             | Ctrl+A                            | Ctrl+A                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Deselect                                                                  |                                           |                                                    | Ctrl+Shift+A                      | Ctrl+Shift+A           |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Bold                                                                      | Ctrl+B                                    | Ctrl+B                                             | Ctrl+B                            | Ctrl+B                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Italic                                                                    | Ctrl+I                                    | Ctrl+I                                             | Ctrl+I                            | Ctrl+I                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Underline                                                                 | Ctrl+U                                    | Ctrl+U                                             | Ctrl+U                            | Ctrl+U                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToNextChar`           | Right                                     | Right, Meta+F                                      | Right                             | Right                  |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToPreviousChar`       | Left                                      | Left, Meta+B                                       | Left                              | Left                   |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToNextWord`           | Ctrl+Right                                | Alt+Right                                          | Ctrl+Right                        | Ctrl+Right             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToPreviousWord`       | Ctrl+Left                                 | Alt+Left                                           | Ctrl+Left                         | Ctrl+Left              |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToNextLine`           | Down                                      | Down, Meta+N                                       | Down                              | Down                   |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToPreviousLine`       | Up                                        | Up, Meta+P                                         | Up                                | Up                     |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToNextPage`           | PgDown                                    | PgDown, Alt+PgDown, Meta+Down, Meta+PgDown, Meta+V | PgDown                            | PgDown                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToPreviousPage`       | PgUp                                      | PgUp, Alt+PgUp, Meta+Up, Meta+PgUp                 | PgUp                              | PgUp                   |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToStartOfLine`        | Home                                      | Ctrl+Left, Meta+Left                               | Home                              | Home                   |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToEndOfLine`          | End                                       | Ctrl+Right, Meta+Right                             | End, Ctrl+E                       | End, Ctrl+E            |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToStartOfBlock`       | (none)                                    | Alt+Up, Meta+A                                     | (none)                            | (none)                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToEndOfBlock`         | (none)                                    | Alt+Down, Meta+E                                   | (none)                            | (none)                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToStartOfDocument`    | Ctrl+Home                                 | Ctrl+Up, Home                                      | Ctrl+Home                         | Ctrl+Home              |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.MoveToEndOfDocument`      | Ctrl+End                                  | Ctrl+Down, End                                     | Ctrl+End                          | Ctrl+End               |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectNextChar`           | Shift+Right                               | Shift+Right                                        | Shift+Right                       | Shift+Right            |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectPreviousChar`       | Shift+Left                                | Shift+Left                                         | Shift+Left                        | Shift+Left             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectNextWord`           | Ctrl+Shift+Right                          | Alt+Shift+Right                                    | Ctrl+Shift+Right                  | Ctrl+Shift+Right       |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectPreviousWord`       | Ctrl+Shift+Left                           | Alt+Shift+Left                                     | Ctrl+Shift+Left                   | Ctrl+Shift+Left        |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectNextLine`           | Shift+Down                                | Shift+Down                                         | Shift+Down                        | Shift+Down             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectPreviousLine`       | Shift+Up                                  | Shift+Up                                           | Shift+Up                          | Shift+Up               |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectNextPage`           | Shift+PgDown                              | Shift+PgDown                                       | Shift+PgDown                      | Shift+PgDown           |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectPreviousPage`       | Shift+PgUp                                | Shift+PgUp                                         | Shift+PgUp                        | Shift+PgUp             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectStartOfLine`        | Shift+Home                                | Ctrl+Shift+Left                                    | Shift+Home                        | Shift+Home             |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectEndOfLine`          | Shift+End                                 | Ctrl+Shift+Right                                   | Shift+End                         | Shift+End              |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectStartOfBlock`       | (none)                                    | Alt+Shift+Up, Meta+Shift+A                         | (none)                            | (none)                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectEndOfBlock`         | (none)                                    | Alt+Shift+Down, Meta+Shift+E                       | (none)                            | (none)                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectStartOfDocument`    | Ctrl+Shift+Home                           | Ctrl+Shift+Up, Shift+Home                          | Ctrl+Shift+Home                   | Ctrl+Shift+Home        |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.SelectEndOfDocument`      | Ctrl+Shift+End                            | Ctrl+Shift+Down, Shift+End                         | Ctrl+Shift+End                    | Ctrl+Shift+End         |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.DeleteStartOfWord`        | Ctrl+Backspace                            | Alt+Backspace                                      | Ctrl+Backspace                    | Ctrl+Backspace         |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.DeleteEndOfWord`          | Ctrl+Del                                  | (none)                                             | Ctrl+Del                          | Ctrl+Del               |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.DeleteEndOfLine`          | (none)                                    | (none)                                             | Ctrl+K                            | Ctrl+K                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.DeleteCompleteLine`       | (none)                                    | (none)                                             | Ctrl+U                            | Ctrl+U                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.InsertParagraphSeparator` | Enter                                     | Enter                                              | Enter                             | Enter                  |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.InsertLineSeparator`      | Shift+Enter                               | Meta+Enter, Meta+O                                 | Shift+Enter                       | Shift+Enter            |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Backspace                                                                 | (none)                                    | Delete, Meta+H                                     | (none)                            | (none)                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+
| Cancel                                                                    | Escape                                    | Escape, Ctrl+.                                     | Escape                            | Escape                 |
+---------------------------------------------------------------------------+-------------------------------------------+----------------------------------------------------+-----------------------------------+------------------------+

Note that, since the key sequences used for the standard shortcuts differ between platforms, you still need to test your shortcuts on each platform to ensure that you do not unintentionally assign the same key sequence to many actions.

.. _qkeysequence-keyboard-layout-issues:

Keyboard Layout Issues
----------------------

Many key sequence specifications are chosen by developers based on the layout of certain types of keyboard, rather than choosing keys that represent the first letter of an action's name, such as Ctrl S ("Ctrl+S") or Ctrl C ("Ctrl+C"). Additionally, because certain symbols can only be entered with the help of modifier keys on certain keyboard layouts, key sequences intended for use with one keyboard layout may map to a different key, map to no keys at all, or require an additional modifier key to be used on different keyboard layouts.

For example, the shortcuts, Ctrl plus and Ctrl minus, are often used as shortcuts for zoom operations in graphics applications, and these may be specified as "Ctrl++" and "Ctrl+-" respectively. However, the way these shortcuts are specified and interpreted depends on the keyboard layout. Users of Norwegian keyboards will note that the + and - keys are not adjacent on the keyboard, but will still be able to activate both shortcuts without needing to press the Shift key. However, users with British keyboards will need to hold down the Shift key to enter the + symbol, making the shortcut effectively the same as "Ctrl+Shift+=".

Although some developers might resort to fully specifying all the modifiers they use on their keyboards to activate a shortcut, this will also result in unexpected behavior for users of different keyboard layouts.

For example, a developer using a British keyboard may decide to specify "Ctrl+Shift+=" as the key sequence in order to create a shortcut that coincidentally behaves in the same way as Ctrl plus. However, the = key needs to be accessed using the Shift key on Norwegian keyboard, making the required shortcut effectively Ctrl Shift Shift = (an impossible key combination).

As a result, both human-readable strings and hard-coded key codes can both be problematic to use when specifying a key sequence that can be used on a variety of different keyboard layouts. Only the use of :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey` guarantees that the user will be able to use the shortcuts that the developer intended.

Despite this, we can address this issue by ensuring that human-readable strings are used, making it possible for translations of key sequences to be made for users of different languages. This approach will be successful for users whose keyboards have the most typical layout for the language they are using.

.. _qkeysequence-gnu-emacs-style-key-sequences:

GNU Emacs Style Key Sequences
-----------------------------

Key sequences similar to those used in `GNU Emacs <http://www.gnu.org/software/emacs/>`_, allowing up to four key codes, can be created by using the multiple argument constructor, or by passing a human-readable string of comma-separated key sequences.

For example, the key sequence, Ctrl X followed by Ctrl C, can be specified using either of the following ways:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qkeysequence.py
    :lines: 73-75

**Warning:** A :sip:ref:`~PyQt6.QtWidgets.QApplication` instance must have been constructed before a :sip:ref:`~PyQt6.QtGui.QKeySequence` is created; otherwise, your application may crash.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QShortcut`.
