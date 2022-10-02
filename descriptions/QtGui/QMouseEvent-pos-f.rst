.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: d6cf82223c637430f766e0149bf9cd78

Use position() instead.

Returns the position of the mouse cursor, relative to the widget that received the event.

If you move the widget as a result of the mouse event, use the global position returned by globalPos() to avoid a shaking motion.

.. seealso:: x(), y(), globalPos().
