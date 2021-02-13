.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: cfae267349d1e0758dc3f0b48e6a5bfa

Returns the estimated final position for the current scroll movement. Returns the current position if the scroller state is not Scrolling. The result is undefined when the scroller state is Inactive.

The target position is in pixel.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScroller.pixelPerMeter`, :sip:ref:`~PyQt6.QtWidgets.QScroller.scrollTo`.
