.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: () const
    :digest: 6a7bf8078e0f7dc614370152d2bce5f8

This functions returns the current rubber band area (in viewport coordinates) if the user is currently doing an itemselection with rubber band. When the user is not using the rubber band this functions returns (a null) QRectF().

Notice that part of this :sip:ref:`~PyQt6.QtCore.QRect` can be outise the visual viewport. It can e.g contain negative values.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.rubberBandSelectionMode`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.rubberBandChanged`.
