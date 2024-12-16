.. sip:class-description::
    :status: todo
    :brief: Radio button with a text label
    :digest: c50e12f8f195e0dba21e5aa691169655

The :sip:ref:`~PyQt6.QtWidgets.QRadioButton` widget provides a radio button with a text label.

.. image:: ../../../images/fusion-radiobutton.png

A :sip:ref:`~PyQt6.QtWidgets.QRadioButton` is an option button that can be switched on (checked) or off (unchecked). Radio buttons typically present the user with a "one of many" choice. In a group of radio buttons, only one radio button at a time can be checked; if the user selects another button, the previously selected button is switched off.

Radio buttons are autoExclusive by default. If auto-exclusive is enabled, radio buttons that belong to the same parent widget behave as if they were part of the same exclusive button group. If you need multiple exclusive button groups for radio buttons that belong to the same parent widget, put them into a :sip:ref:`~PyQt6.QtWidgets.QButtonGroup`.

Whenever a button is switched on or off, it emits the toggled() signal. Connect to this signal if you want to trigger an action each time the button changes state. Use isChecked() to see if a particular button is selected.

Just like :sip:ref:`~PyQt6.QtWidgets.QPushButton`, a radio button displays text, and optionally a small icon. The icon is set with setIcon(). The text can be set in the constructor or with setText(). A shortcut key can be specified by preceding the preferred character with an ampersand in the text. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qradiobutton.py
    :lines: 54-54

In this example the shortcut is *Alt+c*. See the QShortcut documentation for details. To display an actual ampersand, use '&&'.

Important inherited members: text(), setText(), text(), setDown(), isDown(), autoRepeat(), group(), setAutoRepeat(), toggle(), pressed(), released(), clicked(), and toggled().

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPushButton`, :sip:ref:`~PyQt6.QtWidgets.QToolButton`, :sip:ref:`~PyQt6.QtWidgets.QCheckBox`.
