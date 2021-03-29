.. sip:method-description::
    :status: todo
    :pysig: 7905de75ba1096b008e853dc1ed418eb
    :realsig: (QShowEvent*)
    :digest: 08930fd564af14fe566c14d27567dfd6

Override this to handle show events (\ *ev*).

The function is called when the window has requested becoming visible.

If the window is successfully shown by the windowing system, this will be followed by a resize and an expose event.
