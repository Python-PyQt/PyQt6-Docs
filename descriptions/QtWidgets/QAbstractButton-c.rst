.. sip:class-description::
    :status: todo
    :brief: The abstract base class of button widgets, providing functionality common to buttons
    :digest: 79bf8ad06e84401d1285e051f88dcf43

The `QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_ class is the abstract base class of button widgets, providing functionality common to buttons.

This class implements an *abstract* button. Subclasses of this class handle user actions, and specify how the button is drawn.

`QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_ provides support for both push buttons and checkable (toggle) buttons. Checkable buttons are implemented in the :sip:ref:`~PyQt6.QtWidgets.QRadioButton` and :sip:ref:`~PyQt6.QtWidgets.QCheckBox` classes. Push buttons are implemented in the :sip:ref:`~PyQt6.QtWidgets.QPushButton` and :sip:ref:`~PyQt6.QtWidgets.QToolButton` classes; these also provide toggle behavior if required.

Any button can display a label containing text and an icon. :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setText` sets the text; :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setIcon` sets the icon. If a button is disabled, its label is changed to give the button a "disabled" appearance.

If the button is a text button with a string containing an ampersand ('&'), `QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_ automatically creates a shortcut key. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qabstractbutton.py
    :lines: 54-54

The Alt+C shortcut is assigned to the button, i.e., when the user presses Alt+C the button will call :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.animateClick`. See the QShortcut documentation for details. To display an actual ampersand, use '&&'.

You can also set a custom shortcut key using the :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setShortcut` function. This is useful mostly for buttons that do not have any text, and therefore can't have any automatic shortcut.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qabstractbutton.py
    :lines: 59-60

All the buttons provided by Qt (\ :sip:ref:`~PyQt6.QtWidgets.QPushButton`, :sip:ref:`~PyQt6.QtWidgets.QToolButton`, :sip:ref:`~PyQt6.QtWidgets.QCheckBox`, and :sip:ref:`~PyQt6.QtWidgets.QRadioButton`) can display both :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.text` and `icons <https://doc.qt.io/qt-6/stylesheet-reference.html#icon>`_.

A button can be made the default button in a dialog by means of :sip:ref:`~PyQt6.QtWidgets.QPushButton.setDefault` and :sip:ref:`~PyQt6.QtWidgets.QPushButton.setAutoDefault`.

`QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_ provides most of the states used for buttons:

* :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isDown` indicates whether the button is *pressed* down.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isChecked` indicates whether the button is *checked*. Only checkable buttons can be checked and unchecked (see below).

* isEnabled() indicates whether the button can be pressed by the user.

  **Note:** As opposed to other widgets, buttons derived from `QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_ accept mouse and context menu events when disabled.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setAutoRepeat` sets whether the button will auto-repeat if the user holds it down. :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.autoRepeatDelay` and :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.autoRepeatInterval` define how auto-repetition is done.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setCheckable` sets whether the button is a toggle button or not.

The difference between :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isDown` and :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isChecked` is as follows. When the user clicks a toggle button to check it, the button is first *pressed* then released into the *checked* state. When the user clicks it again (to uncheck it), the button moves first to the *pressed* state, then to the *unchecked* state (\ :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isChecked` and :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.isDown` are both false).

`QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_ provides four signals:

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.pressed` is emitted when the left mouse button is pressed while the mouse cursor is inside the button.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.released` is emitted when the left mouse button is released.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.clicked` is emitted when the button is first pressed and then released, when the shortcut key is typed, or when :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.click` or :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.animateClick` is called.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.toggled` is emitted when the state of a toggle button changes.

To subclass `QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_, you must reimplement at least :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.paintEvent` to draw the button's outline and its text or pixmap. It is generally advisable to reimplement sizeHint() as well, and sometimes :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.hitButton` (to determine whether a button press is within the button). For buttons with more than two states (like tri-state buttons), you will also have to reimplement :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.checkStateSet` and :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.nextCheckState`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QButtonGroup`.
