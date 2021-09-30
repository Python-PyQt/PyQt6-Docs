.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: 9df76c24ce88ec077b9c39710d48efeb

Returns the position of the mouse cursor, relative to the widget that received the event.

If you move the widget as a result of the mouse event, use the global position returned by  to avoid a shaking motion.

.. seealso:: x(), y(), globalPos().
