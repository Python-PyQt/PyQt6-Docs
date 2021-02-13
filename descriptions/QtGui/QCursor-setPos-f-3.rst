.. sip:method-description::
    :status: todo
    :pysig: 195120c75a320932fd94bb3c8cc232d3
    :realsig: (QScreen*,int,int)
    :digest: 2e70339307e8b121292c4e61528d0c05

Moves the cursor (hot spot) of the *screen* to the global screen position (\ *x*, *y*).

You can call :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal` to translate widget coordinates to global screen coordinates.

**Note:** Calling this function results in changing the cursor position through the windowing system. The windowing system will typically respond by sending mouse events to the application's window. This means that the usage of this function should be avoided in unit tests and everywhere where fake mouse events are being injected via QWindowSystemInterface because the windowing system's mouse state (with regards to buttons for example) may not match the state in the application-generated events.

**Note:** On platforms where there is no windowing system or cursors are not available, this function may do nothing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QCursor.pos`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapFromGlobal`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`.
