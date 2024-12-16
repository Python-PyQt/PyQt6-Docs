.. sip:method-description::
    :status: todo
    :pysig: d409847c33b4369753f8b837c22758e9
    :realsig: ()
    :digest: 420db19022c036d7cb2295fa5e0bac9a

Returns a list of names of supported codecs. The names returned by this function can be passed to :sip:ref:`~PyQt6.QtCore.QStringEncoder`'s and :sip:ref:`~PyQt6.QtCore.QStringDecoder`'s constructor to create a en- or decoder for the given codec.

This function may be used to obtain a listing of additional codecs beyond the standard ones. Support for additional codecs requires Qt be compiled with support for the ICU library.

**Note:** The order of codecs is an internal implementation detail and not guaranteed to be stable.
