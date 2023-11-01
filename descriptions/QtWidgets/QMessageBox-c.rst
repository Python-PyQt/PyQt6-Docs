.. sip:class-description::
    :status: todo
    :brief: Modal dialog for informing the user or for asking the user a question and receiving an answer
    :digest: 83eedead3c6864bfa946c1bcd88a7ada

The :sip:ref:`~PyQt6.QtWidgets.QMessageBox` class provides a modal dialog for informing the user or for asking the user a question and receiving an answer.

A message box displays a primary :sip:ref:`~PyQt6.QtWidgets.QMessageBox.text` to alert the user to a situation, an :sip:ref:`~PyQt6.QtWidgets.QMessageBox.informativeText` to further explain the situation, and an optional :sip:ref:`~PyQt6.QtWidgets.QMessageBox.detailedText` to provide even more data if the user requests it.

A message box can also display an :sip:ref:`~PyQt6.QtWidgets.QMessageBox.icon` and :sip:ref:`~PyQt6.QtWidgets.QMessageBox.standardButtons` for accepting a user response.

Two APIs for using :sip:ref:`~PyQt6.QtWidgets.QMessageBox` are provided, the property-based API, and the static functions. Calling one of the static functions is the simpler approach, but it is less flexible than using the property-based API, and the result is less informative. Using the property-based API is recommended.

.. _qmessagebox-the-property-based-api:

The Property-based API
----------------------

To use the property-based API, construct an instance of :sip:ref:`~PyQt6.QtWidgets.QMessageBox`, set the desired properties, and call exec() to show the message. The simplest configuration is to set only the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.text` property.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qmessagebox.py
    :lines: 122-124

The user must click the OK button to dismiss the message box. The rest of the GUI is blocked until the message box is dismissed.

.. image:: ../../../images/msgbox1.png

A better approach than just alerting the user to an event is to also ask the user what to do about it.

Set the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.standardButtons` property to the set of buttons you want as the set of user responses. The buttons are specified by combining values from StandardButtons using the bitwise OR operator. The display order for the buttons is platform-dependent. For example, on Windows, Save is displayed to the left of Cancel, whereas on macOS, the order is reversed. Mark one of your standard buttons to be your :sip:ref:`~PyQt6.QtWidgets.QMessageBox.defaultButton`.

The :sip:ref:`~PyQt6.QtWidgets.QMessageBox.informativeText` property can be used to add additional context to help the user choose the appropriate action.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qmessagebox.py
    :lines: 128-133

.. image:: ../../../images/msgbox2.png

The exec() slot returns the StandardButtons value of the button that was clicked.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qmessagebox.py
    :lines: 137-150

To give the user more information to help them choose the appropriate, action, set the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.detailedText` property. Depending on the platform the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.detailedText`, may require the user to click a Show Details... button to be shown.

.. image:: ../../../images/msgbox3.png

Clicking the Show Details... button displays the detailed text.

.. image:: ../../../images/msgbox4.png

.. _qmessagebox-rich-text-and-the-text-format-property:

Rich Text and the Text Format Property
......................................

The :sip:ref:`~PyQt6.QtWidgets.QMessageBox.detailedText` property is always interpreted as plain text. The :sip:ref:`~PyQt6.QtWidgets.QMessageBox.text` and :sip:ref:`~PyQt6.QtWidgets.QMessageBox.informativeText` properties can be either plain text or rich text. These strings are interpreted according to the setting of the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.textFormat` property. The default setting is :sip:ref:`~PyQt6.QtCore.Qt.TextFormat.AutoText`.

Note that for some plain text strings containing XML meta-characters, the auto-text rich text detection test may fail causing your plain text string to be interpreted incorrectly as rich text. In these rare cases, use Qt::convertFromPlainText() to convert your plain text string to a visually equivalent rich text string, or set the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.textFormat` property explicitly with :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setTextFormat`.

.. _qmessagebox-severity-levels-and-the-icon-and-pixmap-properties:

Severity Levels and the Icon and Pixmap Properties
..................................................

:sip:ref:`~PyQt6.QtWidgets.QMessageBox` supports four predefined message severity levels, or message types, which really only differ in the predefined icon they each show. Specify one of the four predefined message types by setting the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.icon` property to one of the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon`. The following rules are guidelines:

+--------------------------------------------------+----------------------------------------------------------+----------------------------------------------------+
| .. image:: ../../../images/qmessagebox-quest.png | :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Question`    | For asking a question during normal operations.    |
+--------------------------------------------------+----------------------------------------------------------+----------------------------------------------------+
| .. image:: ../../../images/qmessagebox-info.png  | :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Information` | For reporting information about normal operations. |
+--------------------------------------------------+----------------------------------------------------------+----------------------------------------------------+
| .. image:: ../../../images/qmessagebox-warn.png  | :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Warning`     | For reporting non-critical errors.                 |
+--------------------------------------------------+----------------------------------------------------------+----------------------------------------------------+
| .. image:: ../../../images/qmessagebox-crit.png  | :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.Critical`    | For reporting critical errors.                     |
+--------------------------------------------------+----------------------------------------------------------+----------------------------------------------------+

:sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon` are not defined by :sip:ref:`~PyQt6.QtWidgets.QMessageBox`, but provided by the style. The default value is :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon.NoIcon`. The message boxes are otherwise the same for all cases. When using a standard icon, use the one recommended in the table, or use the one recommended by the style guidelines for your platform. If none of the standard icons is right for your message box, you can use a custom icon by setting the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.iconPixmap` property instead of setting the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.icon` property.

In summary, to set an icon, use *either* :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setIcon` for one of the standard icons, *or* :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setIconPixmap` for a custom icon.

.. _qmessagebox-the-static-functions-api:

The Static Functions API
------------------------

Building message boxes with the static functions API, although convenient, is less flexible than using the property-based API, because the static function signatures lack parameters for setting the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.informativeText` and :sip:ref:`~PyQt6.QtWidgets.QMessageBox.detailedText` properties. One work-around for this has been to use the ``title`` parameter as the message box main text and the ``text`` parameter as the message box informative text. Because this has the obvious drawback of making a less readable message box, platform guidelines do not recommend it. The *Microsoft Windows User Interface Guidelines* recommend using the :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationName` as the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setWindowTitle`, which means that if you have an informative text in addition to your main text, you must concatenate it to the ``text`` parameter.

Note that the static function signatures have changed with respect to their button parameters, which are now used to set the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.standardButtons` and the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.defaultButton`.

Static functions are available for creating :sip:ref:`~PyQt6.QtWidgets.QMessageBox.information`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.question`, :sip:ref:`~PyQt6.QtWidgets.QMessageBox.warning`, and :sip:ref:`~PyQt6.QtWidgets.QMessageBox.critical` message boxes.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qmessagebox.py
    :lines: 54-59

The `Standard Dialogs <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_ example shows how to use :sip:ref:`~PyQt6.QtWidgets.QMessageBox` and the other built-in Qt dialogs.

.. _qmessagebox-advanced-usage:

Advanced Usage
--------------

If the standard buttons are not flexible enough for your message box, you can use the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.addButton` overload that takes a text and a :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole.ButtonRole` to add custom buttons. The :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole.ButtonRole` is used by :sip:ref:`~PyQt6.QtWidgets.QMessageBox` to determine the ordering of the buttons on screen (which varies according to the platform). You can test the value of :sip:ref:`~PyQt6.QtWidgets.QMessageBox.clickedButton` after calling exec(). For example,

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qmessagebox.py
    :lines: 81-91

.. _qmessagebox-default-and-escape-keys:

Default and Escape Keys
-----------------------

The default button (i.e., the button activated when Enter is pressed) can be specified using :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setDefaultButton`. If a default button is not specified, :sip:ref:`~PyQt6.QtWidgets.QMessageBox` tries to find one based on the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole.ButtonRole` of the buttons used in the message box.

The escape button (the button activated when Esc is pressed) can be specified using :sip:ref:`~PyQt6.QtWidgets.QMessageBox.setEscapeButton`. If an escape button is not specified, :sip:ref:`~PyQt6.QtWidgets.QMessageBox` tries to find one using these rules:

#. If there is only one button, it is the button activated when Esc is pressed.

#. If there is a :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.Cancel` button, it is the button activated when Esc is pressed.

#. If there is exactly one button having either :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole.RejectRole` or the :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole.NoRole`, it is the button activated when Esc is pressed.

When an escape button can't be determined using these rules, pressing Esc has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox`, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
