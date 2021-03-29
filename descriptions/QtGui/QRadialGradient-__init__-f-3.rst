.. sip:method-description::
    :status: todo
    :pysig: 8f3e456cf87b63fe830da17b52cfc608
    :realsig: (const QPointF&,qreal,const QPointF&)
    :digest: da9190de4c7d48e6d887566a7ec5d77e

Constructs a simple radial gradient with the given *center*, *radius* and *focalPoint*.

**Note:** If the given focal point is outside the circle defined by the *center* point and *radius*, it will be re-adjusted to lie at a point on the circle where it intersects with the line from *center* to *focalPoint*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGradient.setColorAt`, :sip:ref:`~PyQt6.QtGui.QGradient.setStops`.
