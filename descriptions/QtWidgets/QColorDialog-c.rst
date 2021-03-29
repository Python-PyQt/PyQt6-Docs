.. sip:class-description::
    :status: todo
    :brief: Dialog widget for specifying colors
    :digest: 9b8fcb3d6acfa4c122c9d37307ae53b6

The :sip:ref:`~PyQt6.QtWidgets.QColorDialog` class provides a dialog widget for specifying colors.

The color dialog's function is to allow users to choose colors. For example, you might use this in a drawing program to allow the user to set the brush color.

The static functions provide modal color dialogs.

The static :sip:ref:`~PyQt6.QtWidgets.QColorDialog.getColor` function shows the dialog, and allows the user to specify a color. This function can also be used to let users choose a color with a level of transparency: pass the :sip:ref:`~PyQt6.QtWidgets.QColorDialog.ColorDialogOptions.ShowAlphaChannel` option as an additional argument.

The user can store :sip:ref:`~PyQt6.QtWidgets.QColorDialog.customCount` different custom colors. The custom colors are shared by all color dialogs, and remembered during the execution of the program. Use :sip:ref:`~PyQt6.QtWidgets.QColorDialog.setCustomColor` to set the custom colors, and use :sip:ref:`~PyQt6.QtWidgets.QColorDialog.customColor` to get them.

When pressing the "Pick Screen Color" button, the cursor changes to a haircross and the colors on the screen are scanned. The user can pick up one by clicking the mouse or the Enter button. Pressing Escape restores the last color selected before entering this mode.

The `Standard Dialogs <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_ example shows how to use :sip:ref:`~PyQt6.QtWidgets.QColorDialog` as well as other built-in Qt dialogs.

.. image:: ../../../images/fusion-colordialog.png

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog`, :sip:ref:`~PyQt6.QtWidgets.QFontDialog`, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
