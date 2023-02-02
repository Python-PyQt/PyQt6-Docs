.. sip:method-description::
    :status: todo
    :pysig: db89c547bddf0273a709d435967f16f1
    :realsig: (WId)
    :digest: 6b2d074008c7ebf13376156eeb90b981

Returns a pointer to the widget with window identifier/handle *id*.

The window identifier type depends on the underlying window system, see ``qwindowdefs.h`` for the actual definition. If there is no widget with this identifier, ``nullptr`` is returned.
