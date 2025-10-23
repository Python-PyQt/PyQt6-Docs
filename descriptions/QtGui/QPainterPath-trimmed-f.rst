.. sip:method-description::
    :status: todo
    :pysig: 43d0f4d9d946bc2985e3781e38f72eec
    :realsig: (qreal, qreal, qreal) const
    :digest: ba3260f214c80a944bc1114cdcae872c

Returns the section of the path between the length fractions *fromFraction* and *toFraction*. The effective range of the fractions are from 0, denoting the start point of the path, to 1, denoting its end point. The fractions are linear with respect to path length, in contrast to the percentage *t* values.

The value of *offset* will be added to the fraction values. If that causes an over- or underflow of the [0, 1] range, the values will be wrapped around, as will the resulting path. The effective range of the offset is between -1 and 1.

Repeated calls to this function can be optimized by {enabling caching}{\ :sip:ref:`~PyQt6.QtGui.QPainterPath.setCachingEnabled`}.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.length`, :sip:ref:`~PyQt6.QtGui.QPainterPath.percentAtLength`, :sip:ref:`~PyQt6.QtGui.QPainterPath.setCachingEnabled`.
