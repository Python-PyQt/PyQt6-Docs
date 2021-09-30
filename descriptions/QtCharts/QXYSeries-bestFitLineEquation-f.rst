.. sip:method-description::
    :status: todo
    :pysig: 7f1aac6c734c09fecd13d8c6d9ef6c84
    :realsig: (bool&) const
    :digest: 17404c247c38bbf136cf3701c7629790

Returns a pair of numbers where the first number is a slope factor and the second number is intercept of a linear function for a best fit line.

Those factors are calculated using Least Squares Method based on points passed to the series.

Parameter *ok* is used to report a failure by setting its value to ``false`` and to report a success by setting its value to ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.bestFitLineVisible`.
