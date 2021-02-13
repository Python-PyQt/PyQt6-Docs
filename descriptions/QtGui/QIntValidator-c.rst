.. sip:class-description::
    :status: todo
    :brief: Validator that ensures a string contains a valid integer within a specified range
    :digest: 29ac936be8a9e00c0e411535ad018c8c

The :sip:ref:`~PyQt6.QtGui.QIntValidator` class provides a validator that ensures a string contains a valid integer within a specified range.

Example of use:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qvalidator.py
    :lines: 66-70

Below we present some examples of validators. In practice they would normally be associated with a widget as in the example above.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qvalidator.py
    :lines: 75-99

Notice that the value ``999`` returns Intermediate. Values consisting of a number of digits equal to or less than the max value are considered intermediate. This is intended because the digit that prevents a number from being in range is not necessarily the last digit typed. This also means that an intermediate number can have leading zeros.

The minimum and maximum values are set in one call with :sip:ref:`~PyQt6.QtGui.QIntValidator.setRange`, or individually with :sip:ref:`~PyQt6.QtGui.QIntValidator.setBottom` and :sip:ref:`~PyQt6.QtGui.QIntValidator.setTop`.

:sip:ref:`~PyQt6.QtGui.QIntValidator` uses its locale() to interpret the number. For example, in Arabic locales, :sip:ref:`~PyQt6.QtGui.QIntValidator` will accept Arabic digits.

**Note:** The QLocale::NumberOptions set on the locale() also affect the way the number is interpreted. For example, since :sip:ref:`~PyQt6.QtCore.QLocale.NumberOptions.RejectGroupSeparator` is not set by default, the validator will accept group separators. It is thus recommended to use :sip:ref:`~PyQt6.QtCore.QLocale.toInt` to obtain the numeric value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDoubleValidator`, :sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator`, :sip:ref:`~PyQt6.QtCore.QLocale.toInt`.
