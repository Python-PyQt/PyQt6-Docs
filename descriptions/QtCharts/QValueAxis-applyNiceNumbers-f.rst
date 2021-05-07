.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f8fa5d02b1ee59f954f4e9858d842516

Modifies the current range and number of tick marks on the axis to look *nice*. The algorithm considers numbers that can be expressed as a form of 1\*10^n, 2\* 10^n, or 5\*10^n to be nice numbers. These numbers are used for setting spacing for the tick marks.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QValueAxis.setRange`, :sip:ref:`~PyQt6.QtCharts.QValueAxis.setTickCount`.
