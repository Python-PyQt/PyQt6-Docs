.. sip:method-description::
    :status: todo
    :pysig: c18d8ec67442dd4267256b61297b928d
    :realsig: (bool*, const QFont&, QWidget*, const QString&, QFontDialog::FontDialogOptions)
    :digest: c5bbbaa7ab8864a9b5f25308be878968

Executes a modal font dialog and returns a font.

If the user clicks OK, the selected font is returned. If the user clicks Cancel, the *initial* font is returned.

The dialog is constructed with the given *parent* and the options specified in *options*. *title* is shown as the window title of the dialog and *initial* is the initially selected font. If the *ok* parameter is not-null, the value it refers to is set to true if the user clicks OK, and set to false if the user clicks Cancel.

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfontdialog.py
    :lines: 72-79

The dialog can also be used to set a widget's font directly:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfontdialog.py
    :lines: 84-84

In this example, if the user clicks OK the font they chose will be used, and if they click Cancel the original font is used.

**Warning:** Do not delete *parent* during the execution of the dialog. If you want to do this, you should create the dialog yourself using one of the :sip:ref:`~PyQt6.QtWidgets.QFontDialog` constructors.
