.. sip:class-description::
    :status: todo
    :brief: Checkbox with a text label
    :digest: 32375b4986d67c51f77e79ecec62d497

The :sip:ref:`~PyQt6.QtWidgets.QCheckBox` widget provides a checkbox with a text label.

.. image:: ../../../images/windows-checkbox.png

A :sip:ref:`~PyQt6.QtWidgets.QCheckBox` is an option button that can be switched on (checked) or off (unchecked). Checkboxes are typically used to represent features in an application that can be enabled or disabled without affecting others. Different types of behavior can be implemented. For example, a :sip:ref:`~PyQt6.QtWidgets.QButtonGroup` can be used to group check buttons logically, allowing exclusive checkboxes. However, :sip:ref:`~PyQt6.QtWidgets.QButtonGroup` does not provide any visual representation.

The image below further illustrates the differences between exclusive and non-exclusive checkboxes.

+----------------------------------+--------------------------------------+
| |image-checkboxes-exclusive-png| | |image-checkboxes-non-exclusive-png| |
+----------------------------------+--------------------------------------+

Whenever a checkbox is checked or cleared, it emits the signal :sip:ref:`~PyQt6.QtWidgets.QCheckBox.stateChanged`. Connect to this signal if you want to trigger an action each time the checkbox changes state. You can use isChecked() to query whether or not a checkbox is checked.

In addition to the usual checked and unchecked states, :sip:ref:`~PyQt6.QtWidgets.QCheckBox` optionally provides a third state to indicate "no change". This is useful whenever you need to give the user the option of neither checking nor unchecking a checkbox. If you need this third state, enable it with :sip:ref:`~PyQt6.QtWidgets.QCheckBox.setTristate`, and use :sip:ref:`~PyQt6.QtWidgets.QCheckBox.checkState` to query the current toggle state.

Just like :sip:ref:`~PyQt6.QtWidgets.QPushButton`, a checkbox displays text, and optionally a small icon. The icon is set with setIcon(). The text can be set in the constructor or with setText(). A shortcut key can be specified by preceding the preferred character with an ampersand. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qcheckbox.py
    :lines: 54-54

In this example, the shortcut is *Alt+A*. See the QShortcut documentation for details. To display an actual ampersand, use '&&'.

Important inherited functions: text(), setText(), text(), pixmap(), setPixmap(), accel(), setAccel(), isToggleButton(), setDown(), isDown(), isOn(), :sip:ref:`~PyQt6.QtWidgets.QCheckBox.checkState`, autoRepeat(), isExclusiveToggle(), group(), setAutoRepeat(), toggle(), pressed(), released(), clicked(), toggled(), :sip:ref:`~PyQt6.QtWidgets.QCheckBox.checkState`, and :sip:ref:`~PyQt6.QtWidgets.QCheckBox.stateChanged`.

.. seealso:: `QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_, :sip:ref:`~PyQt6.QtWidgets.QRadioButton`, `GUI Design Handbook: Check Box <https://doc.qt.io/qt-6/guibooks.html#fowler>`_.

.. |image-checkboxes-exclusive-png| image:: ../../../images/checkboxes-exclusive.png
.. |image-checkboxes-non-exclusive-png| image:: ../../../images/checkboxes-non-exclusive.png
