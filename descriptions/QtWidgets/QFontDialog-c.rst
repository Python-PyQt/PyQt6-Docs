.. sip:class-description::
    :status: todo
    :brief: Dialog widget for selecting a font
    :digest: c3bc6a9d6ad69a20c2e0d19e81f465e0

The :sip:ref:`~PyQt6.QtWidgets.QFontDialog` class provides a dialog widget for selecting a font.

A font dialog is created through one of the static :sip:ref:`~PyQt6.QtWidgets.QFontDialog.getFont` functions.

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfontdialog.py
    :lines: 54-62

The dialog can also be used to set a widget's font directly:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfontdialog.py
    :lines: 67-67

If the user clicks OK the font they chose will be used for myWidget, and if they click Cancel the original font is used.

.. image:: ../../../images/fusion-fontdialog.png

.. seealso:: `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_, :sip:ref:`~PyQt6.QtGui.QFontInfo`, :sip:ref:`~PyQt6.QtGui.QFontMetrics`, :sip:ref:`~PyQt6.QtWidgets.QColorDialog`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog`, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
