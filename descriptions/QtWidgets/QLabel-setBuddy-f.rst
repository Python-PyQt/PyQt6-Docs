.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: fa2eea2459b4fa31388ff9a8d16b531d

Sets this label's buddy to *buddy*.

When the user presses the shortcut key indicated by this label, the keyboard focus is transferred to the label's buddy widget.

The buddy mechanism is only available for QLabels that contain text in which one character is prefixed with an ampersand, '&'. This character is set as the shortcut key. See the :sip:ref:`~PyQt6.QtGui.QKeySequence.mnemonic` documentation for details (to display an actual ampersand, use '&&').

In a dialog, you might create two data entry widgets and a label for each, and set up the geometry layout so each label is just to the left of its data entry widget (its "buddy"), for example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qlabel.py
    :lines: 69-75

With the code above, the focus jumps to the Name field when the user presses Alt+N, and to the Phone field when the user presses Alt+P.

To unset a previously set buddy, call this function with *buddy* set to nullptr.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLabel.buddy`, :sip:ref:`~PyQt6.QtWidgets.QLabel.setText`, :sip:ref:`~PyQt6.QtGui.QShortcut`, :sip:ref:`~PyQt6.QtWidgets.QLabel.setAlignment`.
