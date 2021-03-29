.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: 30c2832888898cb7be42f74b5234be44

Returns the position of the point in this event on the screen or virtual desktop.

**Note:** The global position of a mouse pointer is recorded *at the time of the event*. This is important on asynchronous window systems such as X11; whenever you move your widgets around in response to mouse events,  can differ a lot from the current cursor position returned by :sip:ref:`~PyQt6.QtGui.QCursor.pos`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSinglePointEvent.position`.
