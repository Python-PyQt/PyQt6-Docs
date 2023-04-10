.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 05596906f9f4ad9f1e4eee08aae184f4

Sets the precision of real numbers to *precision*. This value describes the number of fraction digits :sip:ref:`~PyQt6.QtCore.QTextStream` should write when generating real numbers (\ :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.FixedNotation`, :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.ScientificNotation`), or the maximum number of significant digits (\ :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.SmartNotation`).

The precision cannot be a negative value. The default value is 6.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.realNumberPrecision`, :sip:ref:`~PyQt6.QtCore.QTextStream.setRealNumberNotation`.
