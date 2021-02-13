.. sip:class-description::
    :status: todo
    :brief: Spin box widget that takes doubles
    :digest: 5f36b43f38f773921054ed83585dd97b

The :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` class provides a spin box widget that takes doubles.

:sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` allows the user to choose a value by clicking the up and down buttons or by pressing Up or Down on the keyboard to increase or decrease the value currently displayed. The user can also type the value in manually. The spin box supports double values but can be extended to use different strings with :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.validate`, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.textFromValue` and :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.valueFromText`.

Every time the value changes :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` emits :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.valueChanged` and :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.textChanged` signals, the former providing a double and the latter a QString. The :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.textChanged` signal provides the value with both :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.prefix` and :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.suffix`. The current value can be fetched with :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.value` and set with :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setValue`.

Note: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` will round numbers so they can be displayed with the current precision. In a :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` with decimals set to 2, calling :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setValue`\ (2.555) will cause :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.value` to return 2.56.

Clicking the up and down buttons or using the keyboard accelerator's Up and Down arrows will increase or decrease the current value in steps of size :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.singleStep`. If you want to change this behavior you can reimplement the virtual function stepBy(). The minimum and maximum value and the step size can be set using one of the constructors, and can be changed later with :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setMinimum`, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setMaximum` and :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setSingleStep`. The spinbox has a default precision of 2 decimal places but this can be changed using :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setDecimals`.

Most spin boxes are directional, but :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` can also operate as a circular spin box, i.e. if the range is 0.0-99.9 and the current value is 99.9, clicking "up" will give 0 if wrapping() is set to true. Use setWrapping() if you want circular behavior.

The displayed value can be prepended and appended with arbitrary strings indicating, for example, currency or the unit of measurement. See :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setPrefix` and :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.setSuffix`. The text in the spin box is retrieved with text() (which includes any :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.prefix` and :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.suffix`), or with :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.cleanText` (which has no :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.prefix`, no :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.suffix` and no leading or trailing whitespace).

It is often desirable to give the user a special (often default) choice in addition to the range of numeric values. See setSpecialValueText() for how to do this with :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox`.

**Note:** The displayed value of the :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` is limited to 18 characters in addition to eventual prefix and suffix content. This limitation is used to keep the double spin box usable even with extremely large values.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`, :sip:ref:`~PyQt6.QtWidgets.QSlider`, `Spin Boxes Example <https://doc.qt.io/qt-6/qtwidgets-widgets-spinboxes-example.html>`_.
