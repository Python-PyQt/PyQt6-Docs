.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 99fb229c5b44adab66c467b81b294e9c

Displays the number represented by the string *s*.

This version of the function disregards :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.mode` and :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.smallDecimalPoint`.

These digits and other symbols can be shown: 0/O, 1, 2, 3, 4, 5/S, 6, 7, 8, 9/g, minus, decimal point, A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y, colon, degree sign (which is specified as single quote in the string) and space. :sip:ref:`~PyQt6.QtWidgets.QLCDNumber` substitutes spaces for illegal characters.
