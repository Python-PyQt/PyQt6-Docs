.. sip:method-description::
    :status: todo
    :pysig: bc6957ad5250b690f009497f4a7174d3
    :realsig: (const QVariant&,const QVariant&,qreal) const
    :digest: 6a3602ef033fad577fd01e931a6b17d9

This virtual function returns the linear interpolation between variants *from* and *to*, at *progress*, usually a value between 0 and 1. You can reimplement this function in a subclass of :sip:ref:`~PyQt6.QtCore.QVariantAnimation` to provide your own interpolation algorithm.

Note that in order for the interpolation to work with a :sip:ref:`~PyQt6.QtCore.QEasingCurve` that return a value smaller than 0 or larger than 1 (such as :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.InBack`) you should make sure that it can extrapolate. If the semantic of the datatype does not allow extrapolation this function should handle that gracefully.

You should call the :sip:ref:`~PyQt6.QtCore.QVariantAnimation` implementation of this function if you want your class to handle the types already supported by Qt (see class :sip:ref:`~PyQt6.QtCore.QVariantAnimation` description for a list of supported types).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEasingCurve`.
