.. sip:method-description::
    :status: todo
    :pysig: 2f43b333b94ca502018fc8bfc47a8224
    :realsig: (double) const
    :digest: 5048163763576e1f2534f1f2302052e9

This virtual function is used by the spin box whenever it needs to display the given *value*. The default implementation returns a string containing *value* printed using :sip:ref:`~PyQt6.QtWidgets.QWidget.locale`.toString(\ *value*, ``u'f'``, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.decimals`) and will remove the thousand separator unless setGroupSeparatorShown() is set. Reimplementations may return anything.

Note: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` does not call this function for specialValueText() and that neither :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.prefix` nor :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.suffix` should be included in the return value.

If you reimplement this, you may also need to reimplement :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.valueFromText`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox.valueFromText`, :sip:ref:`~PyQt6.QtCore.QLocale.groupSeparator`.
