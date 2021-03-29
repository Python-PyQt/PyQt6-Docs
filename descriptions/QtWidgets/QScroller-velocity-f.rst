.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: d22e6730a68d96fe67cc5800a7f848a7

Returns the current scrolling velocity in meter per second when the state is Scrolling or Dragging. Returns a zero velocity otherwise.

The velocity is reported for both the x and y axis separately by using a :sip:ref:`~PyQt6.QtCore.QPointF`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScroller.pixelPerMeter`.
