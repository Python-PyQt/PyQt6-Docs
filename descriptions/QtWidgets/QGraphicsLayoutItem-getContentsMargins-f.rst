.. sip:method-description::
    :status: todo
    :pysig: 5fd70130e629f44666196fc320d4f2e1
    :realsig: (qreal*,qreal*,qreal*,qreal*) const
    :digest: ed70a99f2138d8dc1b7189f2ec719342

This virtual function provides the *left*, *top*, *right* and *bottom* contents margins for this :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem`. The default implementation assumes all contents margins are 0. The parameters point to values stored in qreals. If any of the pointers is ``nullptr``, that value will not be updated.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setContentsMargins`.
