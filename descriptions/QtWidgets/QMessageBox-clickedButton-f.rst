.. sip:method-description::
    :status: todo
    :pysig: f46cc8bb8d9029504f83ecdd62d53e40
    :realsig: () const
    :digest: f255bba909e41b42151651e5f9e211be

Returns the button that was clicked by the user, or ``nullptr`` if the user hit the Esc key and no :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setEscapeButton` was set.

If exec() hasn't been called yet, returns nullptr.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qmessagebox.py
    :lines: 96-103

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.standardButton`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.button`.
