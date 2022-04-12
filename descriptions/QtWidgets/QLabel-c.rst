.. sip:class-description::
    :status: todo
    :brief: Text or image display
    :digest: 8911998b63bdf171a48c9665caf9e25b

The :sip:ref:`~PyQt6.QtWidgets.QLabel` widget provides a text or image display.

.. image:: ../../../images/windows-label.png

:sip:ref:`~PyQt6.QtWidgets.QLabel` is used for displaying text or an image. No user interaction functionality is provided. The visual appearance of the label can be configured in various ways, and it can be used for specifying a focus mnemonic key for another widget.

A :sip:ref:`~PyQt6.QtWidgets.QLabel` can contain any of the following content types:

+------------+--------------------------------------------------------------------------------------------------------------------+
| Content    | Setting                                                                                                            |
+============+====================================================================================================================+
| Plain text | Pass a QString to :sip:ref:`~PyQt6.QtWidgets.QLabel.setText`.                                                      |
+------------+--------------------------------------------------------------------------------------------------------------------+
| Rich text  | Pass a QString that contains rich text to :sip:ref:`~PyQt6.QtWidgets.QLabel.setText`.                              |
+------------+--------------------------------------------------------------------------------------------------------------------+
| A pixmap   | Pass a :sip:ref:`~PyQt6.QtGui.QPixmap` to :sip:ref:`~PyQt6.QtWidgets.QLabel.setPixmap`.                            |
+------------+--------------------------------------------------------------------------------------------------------------------+
| A movie    | Pass a :sip:ref:`~PyQt6.QtGui.QMovie` to :sip:ref:`~PyQt6.QtWidgets.QLabel.setMovie`.                              |
+------------+--------------------------------------------------------------------------------------------------------------------+
| A number   | Pass an *int* or a *double* to :sip:ref:`~PyQt6.QtWidgets.QLabel.setNum`, which converts the number to plain text. |
+------------+--------------------------------------------------------------------------------------------------------------------+
| Nothing    | The same as an empty plain text. This is the default. Set by :sip:ref:`~PyQt6.QtWidgets.QLabel.clear`.             |
+------------+--------------------------------------------------------------------------------------------------------------------+

**Warning:** When passing a QString to the constructor or calling :sip:ref:`~PyQt6.QtWidgets.QLabel.setText`, make sure to sanitize your input, as :sip:ref:`~PyQt6.QtWidgets.QLabel` tries to guess whether it displays the text as plain text or as rich text, a subset of HTML 4 markup. You may want to call :sip:ref:`~PyQt6.QtWidgets.QLabel.setTextFormat` explicitly, e.g. in case you expect the text to be in plain format but cannot control the text source (for instance when displaying data loaded from the Web).

When the content is changed using any of these functions, any previous content is cleared.

By default, labels display `left-aligned, vertically-centered <https://doc.qt.io/qt-6/stylesheet-reference.html#alignment>`_ text and images, where any tabs in the text to be displayed are :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextExpandTabs`. However, the look of a :sip:ref:`~PyQt6.QtWidgets.QLabel` can be adjusted and fine-tuned in several ways.

The positioning of the content within the :sip:ref:`~PyQt6.QtWidgets.QLabel` widget area can be tuned with :sip:ref:`~PyQt6.QtWidgets.QLabel.setAlignment` and :sip:ref:`~PyQt6.QtWidgets.QLabel.setIndent`. Text content can also wrap lines along word boundaries with :sip:ref:`~PyQt6.QtWidgets.QLabel.setWordWrap`. For example, this code sets up a sunken panel with a two-line text in the bottom right corner (both lines being flush with the right side of the label):

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qlabel.py
    :lines: 54-57

The properties and functions :sip:ref:`~PyQt6.QtWidgets.QLabel` inherits from :sip:ref:`~PyQt6.QtWidgets.QFrame` can also be used to specify the widget frame to be used for any given label.

A :sip:ref:`~PyQt6.QtWidgets.QLabel` is often used as a label for an interactive widget. For this use :sip:ref:`~PyQt6.QtWidgets.QLabel` provides a useful mechanism for adding an mnemonic (see :sip:ref:`~PyQt6.QtGui.QKeySequence`) that will set the keyboard focus to the other widget (called the :sip:ref:`~PyQt6.QtWidgets.QLabel`'s "buddy"). For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qlabel.py
    :lines: 62-64

In this example, keyboard focus is transferred to the label's buddy (the :sip:ref:`~PyQt6.QtWidgets.QLineEdit`) when the user presses Alt+P. If the buddy was a button (inheriting from :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`), triggering the mnemonic would emulate a button click.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, :sip:ref:`~PyQt6.QtGui.QPixmap`, :sip:ref:`~PyQt6.QtGui.QMovie`.
