.. sip:class-description::
    :status: todo
    :brief: Spinbox and a line edit to display values
    :digest: 6de70e69c6c2138643701f4a50c0fee9

The :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` class provides a spinbox and a line edit to display values.

The class is designed as a common super class for widgets like :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` and :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`

Here are the main properties of the class:

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.text`: The text that is displayed in the :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox`.

#. `alignment <https://doc.qt.io/qt-6/stylesheet-reference.html#alignment>`_: The alignment of the text in the :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox`.

#. :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.wrapping`: Whether the :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` wraps from the minimum value to the maximum value and vice versa.

:sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` provides a virtual :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.stepBy` function that is called whenever the user triggers a step. This function takes an integer value to signify how many steps were taken. E.g. Pressing :sip:ref:`~PyQt6.QtCore.Qt.Key.Key_Down` will trigger a call to :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.stepBy`\ (-1).

When the user triggers a step whilst holding the :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers.ControlModifier`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` steps by 10 instead of making a single step. This step modifier affects wheel events, key events and interaction with the spinbox buttons. Note that on macOS, Control corresponds to the Command key.

Since Qt 5.12, :sip:ref:`~PyQt6.QtWidgets.QStyle.StyleHint.SH_SpinBox_StepModifier` can be used to select which :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers` increases the step rate. :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers.NoModifier` disables this feature.

:sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` also provide a virtual function :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.stepEnabled` to determine whether stepping up/down is allowed at any point. This function returns a bitset of StepEnabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`, `Spin Boxes Example <https://doc.qt.io/qt-6/qtwidgets-widgets-spinboxes-example.html>`_.
