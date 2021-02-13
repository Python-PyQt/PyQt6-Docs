.. sip:class-description::
    :status: todo
    :brief: Displays a number with LCD-like digits
    :digest: 1e523f5e6797c53be38602a01b4bfbad

The :sip:ref:`~PyQt6.QtWidgets.QLCDNumber` widget displays a number with LCD-like digits.

.. image:: ../../../images/windows-lcdnumber.png

It can display a number in just about any size. It can display decimal, hexadecimal, octal or binary numbers. It is easy to connect to data sources using the :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.display` slot, which is overloaded to take any of five argument types.

There are also slots to change the base with :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.setMode` and the decimal point with :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.setSmallDecimalPoint`.

:sip:ref:`~PyQt6.QtWidgets.QLCDNumber` emits the :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.overflow` signal when it is asked to display something beyond its range. The range is set by :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.setDigitCount`, but :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.setSmallDecimalPoint` also influences it. If the display is set to hexadecimal, octal or binary, the integer equivalent of the value is displayed.

These digits and other symbols can be shown: 0/O, 1, 2, 3, 4, 5/S, 6, 7, 8, 9/g, minus, decimal point, A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y, colon, degree sign (which is specified as single quote in the string) and space. :sip:ref:`~PyQt6.QtWidgets.QLCDNumber` substitutes spaces for illegal characters.

It is not possible to retrieve the contents of a :sip:ref:`~PyQt6.QtWidgets.QLCDNumber` object, although you can retrieve the numeric value with :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.value`. If you really need the text, we recommend that you connect the signals that feed the :sip:ref:`~PyQt6.QtWidgets.QLCDNumber.display` slot to another slot as well and store the value there.

Incidentally, :sip:ref:`~PyQt6.QtWidgets.QLCDNumber` is the very oldest part of Qt, tracing its roots back to a BASIC program on the `Sinclair Spectrum <https://doc.qt.io/qt-6/http://www.nvg.ntnu.no/sinclair/computers/zxspectrum/zxspectrum.htm>`_.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLabel`, :sip:ref:`~PyQt6.QtWidgets.QFrame`, `Digital Clock Example <https://doc.qt.io/qt-6/qtwidgets-widgets-digitalclock-example.html>`_, `Tetrix Example <https://doc.qt.io/qt-6/qtwidgets-widgets-tetrix-example.html>`_.
