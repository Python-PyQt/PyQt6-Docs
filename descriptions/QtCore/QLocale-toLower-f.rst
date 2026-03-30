.. sip:method-description::
    :status: todo
    :pysig: 558877a2dde966820eb6e4a9d974f77b
    :realsig: (const QString&) const
    :digest: e1a7212abe7eb5b6720e143f5a6b9640

Returns a lowercase copy of *str*.

If Qt Core is using the ICU libraries, they will be used to perform the transformation according to the rules of the current locale. Otherwise the conversion may be done in a platform-dependent manner, with QString::toLower() as a generic fallback.

.. seealso:: QString::toLower().
