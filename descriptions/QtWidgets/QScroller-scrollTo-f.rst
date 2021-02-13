.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: (const QPointF&)
    :digest: dcb5149ea5aaea2fe7416a0a4c532cef

Starts scrolling the widget so that point *pos* is at the top-left position in the viewport.

The behaviour when scrolling outside the valid scroll area is undefined. In this case the scroller might or might not overshoot.

The scrolling speed will be calculated so that the given position will be reached after a platform-defined time span.

*pos* is given in viewport coordinates.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScroller.ensureVisible`.
