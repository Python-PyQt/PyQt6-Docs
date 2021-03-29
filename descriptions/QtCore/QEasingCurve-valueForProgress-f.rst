.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (qreal) const
    :digest: cecdfee200a33b84b4f0fd03aec4f6f3

Return the effective progress for the easing curve at *progress*. Whereas *progress* must be between 0 and 1, the returned effective progress can be outside those bounds. For example, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.InBack` will return negative values in the beginning of the function.
