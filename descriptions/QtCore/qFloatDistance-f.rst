.. sip:method-description::
    :status: todo
    :pysig: ed3669ced12cf175d82b06ee109b17de
    :realsig: (double,double)
    :digest: 6bb3639956db12bb6337d736f471693a

Returns the number of representable floating-point numbers between *a* and *b*.

This function serves the same purpose as ``qFloatDistance(float, float)``, but returns the distance between two ``double`` numbers. Since the range is larger than for two ``float`` numbers (``[-DBL_MAX,DBL_MAX]``), the return type is quint64.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qFuzzyCompare`.
