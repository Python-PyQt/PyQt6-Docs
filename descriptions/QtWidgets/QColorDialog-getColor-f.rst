.. sip:method-description::
    :status: todo
    :pysig: b5df8b02a0cd69b7451cd1d732e861af
    :realsig: (const QColor&, QWidget*, const QString&, QColorDialog::ColorDialogOptions)
    :digest: 11b82abb6358977411d53663b990a0ee

Pops up a modal color dialog with the given window *title* (or "Select Color" if none is specified), lets the user choose a color, and returns that color. The color is initially set to *initial*. The dialog is a child of *parent*. It returns an invalid (see :sip:ref:`~PyQt6.QtGui.QColor.isValid`) color if the user cancels the dialog.

The *options* argument allows you to customize the dialog.
