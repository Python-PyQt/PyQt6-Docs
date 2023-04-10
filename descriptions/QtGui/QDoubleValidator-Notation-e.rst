.. sip:enum-description::
    :status: todo
    :digest: 052adcf0f031d280182819c2aed0dcbe

This enum defines the allowed notations for entering a double.

The whole number part may, as usual, include a sign. This, along with the separators for fractional part, exponent and any digit-grouping, depend on locale. :sip:ref:`~PyQt6.QtGui.QDoubleValidator` doesn't check the placement (which would also depend on locale) of any digit-grouping separators it finds, but it will reject input that contains them if :sip:ref:`~PyQt6.QtCore.QLocale.NumberOption.RejectGroupSeparator` is set in ``locale().numberOptions()``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.numberOptions`, :sip:ref:`~PyQt6.QtCore.QLocale.decimalPoint`, :sip:ref:`~PyQt6.QtCore.QLocale.exponential`, :sip:ref:`~PyQt6.QtCore.QLocale.negativeSign`.
