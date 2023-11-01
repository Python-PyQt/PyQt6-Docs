.. sip:class-description::
    :status: todo
    :brief: Spin box widget
    :digest: 158afbd92c90668b1bb8bddb1de5edf6

The :sip:ref:`~PyQt6.QtWidgets.QSpinBox` class provides a spin box widget.

.. image:: ../../../images/windows-spinbox.png

:sip:ref:`~PyQt6.QtWidgets.QSpinBox` is designed to handle integers and discrete sets of values (e.g., month names); use :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` for floating point values.

:sip:ref:`~PyQt6.QtWidgets.QSpinBox` allows the user to choose a value by clicking the up/down buttons or pressing up/down on the keyboard to increase/decrease the value currently displayed. The user can also type the value in manually. The spin box supports integer values but can be extended to use different strings with :sip:ref:`~PyQt6.QtWidgets.QSpinBox.validate`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox.textFromValue` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.valueFromText`.

Every time the value changes :sip:ref:`~PyQt6.QtWidgets.QSpinBox` emits :sip:ref:`~PyQt6.QtWidgets.QSpinBox.valueChanged` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.textChanged` signals, the former providing a int and the latter a QString. The :sip:ref:`~PyQt6.QtWidgets.QSpinBox.textChanged` signal provides the value with both :sip:ref:`~PyQt6.QtWidgets.QSpinBox.prefix` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.suffix`. The current value can be fetched with :sip:ref:`~PyQt6.QtWidgets.QSpinBox.value` and set with :sip:ref:`~PyQt6.QtWidgets.QSpinBox.setValue`.

Clicking the up/down buttons or using the keyboard accelerator's up and down arrows will increase or decrease the current value in steps of size :sip:ref:`~PyQt6.QtWidgets.QSpinBox.singleStep`. If you want to change this behaviour you can reimplement the virtual function stepBy(). The minimum and maximum value and the step size can be set using one of the constructors, and can be changed later with :sip:ref:`~PyQt6.QtWidgets.QSpinBox.setMinimum`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox.setMaximum` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.setSingleStep`.

Most spin boxes are directional, but :sip:ref:`~PyQt6.QtWidgets.QSpinBox` can also operate as a circular spin box, i.e. if the range is 0-99 and the current value is 99, clicking "up" will give 0 if wrapping() is set to true. Use setWrapping() if you want circular behavior.

The displayed value can be prepended and appended with arbitrary strings indicating, for example, currency or the unit of measurement. See :sip:ref:`~PyQt6.QtWidgets.QSpinBox.setPrefix` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.setSuffix`. The text in the spin box is retrieved with text() (which includes any :sip:ref:`~PyQt6.QtWidgets.QSpinBox.prefix` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.suffix`), or with :sip:ref:`~PyQt6.QtWidgets.QSpinBox.cleanText` (which has no :sip:ref:`~PyQt6.QtWidgets.QSpinBox.prefix`, no :sip:ref:`~PyQt6.QtWidgets.QSpinBox.suffix` and no leading or trailing whitespace).

It is often desirable to give the user a special (often default) choice in addition to the range of numeric values. See setSpecialValueText() for how to do this with :sip:ref:`~PyQt6.QtWidgets.QSpinBox`.

.. _qspinbox-subclassing-qspinbox:

Subclassing QSpinBox
--------------------

If using :sip:ref:`~PyQt6.QtWidgets.QSpinBox.prefix`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox.suffix`, and specialValueText() don't provide enough control, you subclass :sip:ref:`~PyQt6.QtWidgets.QSpinBox` and reimplement :sip:ref:`~PyQt6.QtWidgets.QSpinBox.valueFromText` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.textFromValue`. For example, here's the code for a custom spin box that allows the user to enter icon sizes (e.g., "32 x 32"):

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qspinbox.py

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qspinbox.py

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`, :sip:ref:`~PyQt6.QtWidgets.QSlider`, `Spin Boxes Example <https://doc.qt.io/qt-6/qtwidgets-widgets-spinboxes-example.html>`_.
