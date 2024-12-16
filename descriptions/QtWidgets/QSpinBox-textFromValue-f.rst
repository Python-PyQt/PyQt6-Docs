.. sip:method-description::
    :status: todo
    :pysig: d4d85079d3c184e4c59bdc73add11325
    :realsig: (int) const
    :digest: 2b8daa781e02ff1e1583205c80990d15

This virtual function is used by the spin box whenever it needs to display the given *value*. The default implementation returns a string containing *value* printed in the standard way using :sip:ref:`~PyQt6.QtWidgets.QWidget.locale`.toString(), but with the thousand separator removed unless setGroupSeparatorShown() is set. Reimplementations may return anything. (See the example in the detailed description.)

Note: :sip:ref:`~PyQt6.QtWidgets.QSpinBox` does not call this function for specialValueText() and that neither :sip:ref:`~PyQt6.QtWidgets.QSpinBox.prefix` nor :sip:ref:`~PyQt6.QtWidgets.QSpinBox.suffix` should be included in the return value.

If you reimplement this, you may also need to reimplement :sip:ref:`~PyQt6.QtWidgets.QSpinBox.valueFromText` and :sip:ref:`~PyQt6.QtWidgets.QSpinBox.validate`

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSpinBox.valueFromText`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox.validate`, :sip:ref:`~PyQt6.QtCore.QLocale.groupSeparator`.
