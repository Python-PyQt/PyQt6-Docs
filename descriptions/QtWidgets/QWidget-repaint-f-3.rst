.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int,int,int,int)
    :digest: f38de165b6b63784e6a2932505bbcf89

This version repaints a rectangle (\ *x*, *y*, *w*, *h*) inside the widget.

If *w* is negative, it is replaced with ``width() - x``, and if *h* is negative, it is replaced width ``height() - y``.
