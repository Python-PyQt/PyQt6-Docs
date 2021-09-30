.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: d6fd27387f5a318ff5cbdf9cd1da39e8

Sets manual white balance to *colorTemperature*. This is used when :sip:ref:`~PyQt6.QtMultimedia.QCamera.whiteBalanceMode` is set to ``WhiteBalanceManual``. The units are Kelvin.

Setting a color temperature will only have an effect if :sip:ref:`~PyQt6.QtMultimedia.QCamera.WhiteBalanceMode.WhiteBalanceManual` is supported. In this case, setting a temperature greater 0 will automatically set the white balance mode to :sip:ref:`~PyQt6.QtMultimedia.QCamera.WhiteBalanceMode.WhiteBalanceManual`. Setting the temperature to 0 will reset the white balance mode to :sip:ref:`~PyQt6.QtMultimedia.QCamera.WhiteBalanceMode.WhiteBalanceAuto`.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera.colorTemperature`.
