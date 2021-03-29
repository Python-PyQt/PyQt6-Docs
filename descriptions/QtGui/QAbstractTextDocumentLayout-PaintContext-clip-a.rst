.. sip:attribute-description::
    :status: todo
    :digest: c82c373a13647e1f57b2a0eeb8eee32d

This variable holds a hint to the layout specifying the area around paragraphs, frames or text require painting..

Everything outside of this rectangle does not need to be painted.

Specifying a clip rectangle can speed up drawing of large documents significantly. Note that the clip rectangle is in document coordinates (not in viewport coordinates). It is not a substitute for a clip region set on the painter but merely a hint.

The default value is a null rectangle indicating everything needs to be painted.
