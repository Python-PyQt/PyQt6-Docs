.. sip:method-description::
    :status: todo
    :pysig: 9ded2533eac5cb41396fc1246c736daa
    :realsig: (Qt::HighDpiScaleFactorRoundingPolicy)
    :digest: 20b6bbfc5da1023a4b08e4dce64b1032

Sets the high-DPI scale factor rounding policy for the application. The *policy* decides how non-integer scale factors (such as Windows 150%) are handled.

The two principal options are whether fractional scale factors should be rounded to an integer or not. Keeping the scale factor as-is will make the user interface size match the OS setting exactly, but may cause painting errors, for example with the Windows style.

If rounding is wanted, then which type of rounding should be decided next. Mathematically correct rounding is supported but may not give the best visual results: Consider if you want to render 1.5x as 1x ("small UI") or as 2x ("large UI"). See the :sip:ref:`~PyQt6.QtCore.Qt.HighDpiScaleFactorRoundingPolicy` enum for a complete list of all options.

This function must be called before creating the application object. The :sip:ref:`~PyQt6.QtGui.QGuiApplication.highDpiScaleFactorRoundingPolicy` accessor will reflect the environment, if set.

The default value is :sip:ref:`~PyQt6.QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.highDpiScaleFactorRoundingPolicy`.
