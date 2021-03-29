.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&) const
    :digest: 224f65716137348737c6ce921a09907b

Returns an uppercase copy of *str*.

If Qt Core is using the ICU libraries, they will be used to perform the transformation according to the rules of the current locale. Otherwise the conversion may be done in a platform-dependent manner, with QString::toUpper() as a generic fallback.

.. seealso:: QString::toUpper().
