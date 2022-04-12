.. sip:class-description::
    :status: todo
    :brief: Range checking of floating-point numbers
    :digest: 440ac6468cd615052fdb0d52071b47aa

The :sip:ref:`~PyQt6.QtGui.QDoubleValidator` class provides range checking of floating-point numbers.

:sip:ref:`~PyQt6.QtGui.QDoubleValidator` provides an upper bound, a lower bound, and a limit on the number of digits after the decimal point.

You can set the acceptable range in one call with :sip:ref:`~PyQt6.QtGui.QDoubleValidator.setRange`, or with :sip:ref:`~PyQt6.QtGui.QDoubleValidator.setBottom` and :sip:ref:`~PyQt6.QtGui.QDoubleValidator.setTop`. Set the number of decimal places with :sip:ref:`~PyQt6.QtGui.QDoubleValidator.setDecimals`. The :sip:ref:`~PyQt6.QtGui.QDoubleValidator.validate` function returns the validation state.

:sip:ref:`~PyQt6.QtGui.QDoubleValidator` uses its locale() to interpret the number. For example, in the German locale, "1,234" will be accepted as the fractional number 1.234. In Arabic locales, :sip:ref:`~PyQt6.QtGui.QDoubleValidator` will accept Arabic digits.

**Note:** The QLocale::NumberOptions set on the locale() also affect the way the number is interpreted. For example, since :sip:ref:`~PyQt6.QtCore.QLocale.NumberOption.RejectGroupSeparator` is not set by default, the validator will accept group separators. It is thus recommended to use :sip:ref:`~PyQt6.QtCore.QLocale.toDouble` to obtain the numeric value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIntValidator`, :sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator`, :sip:ref:`~PyQt6.QtCore.QLocale.toDouble`, `Line Edits Example <https://doc.qt.io/qt-6/qtwidgets-widgets-lineedits-example.html>`_.
