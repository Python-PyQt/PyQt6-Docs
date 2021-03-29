.. sip:method-description::
    :status: todo
    :pysig: 9e21ebaaa980210ad46bf895a5b92b8d
    :realsig: (WId)
    :digest: ab906c5325f5fd72beccef7ebef03dd2

Returns a pointer to the widget with window identifer/handle *id*.

The window identifier type depends on the underlying window system, see ``qwindowdefs.h`` for the actual definition. If there is no widget with this identifier, ``nullptr`` is returned.
