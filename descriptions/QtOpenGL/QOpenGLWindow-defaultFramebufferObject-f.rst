.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: f2cc04edd038d73a41cd3ffde4cee5e4

The framebuffer object handle used by this window.

When the update behavior is set to ``NoPartialUpdate``, there is no separate framebuffer object. In this case the returned value is the ID of the default framebuffer.

Otherwise the value of the ID of the framebuffer object or ``0`` if not yet initialized.
