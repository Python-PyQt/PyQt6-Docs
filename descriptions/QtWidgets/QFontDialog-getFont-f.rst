.. sip:method-description::
    :status: todo
    :pysig: 4d6f3351df1e0e5481b7e03345c1f4da
    :realsig: (bool*,QWidget*)
    :digest: 2fe4c54ccd16f95269ac38e01b8e4dc5

This is an overloaded function.

Executes a modal font dialog and returns a font.

If the user clicks OK, the selected font is returned. If the user clicks Cancel, the Qt default font is returned.

The dialog is constructed with the given *parent*. If the *ok* parameter is not-null, the value it refers to is set to true if the user clicks OK, and false if the user clicks Cancel.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfontdialog.py
    :lines: 89-96

**Warning:** Do not delete *parent* during the execution of the dialog. If you want to do this, you should create the dialog yourself using one of the :sip:ref:`~PyQt6.QtWidgets.QFontDialog` constructors.
