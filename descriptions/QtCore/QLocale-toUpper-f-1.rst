.. sip:method-description::
    :status: todo
    :pysig: 4fa0960f626986883b81c619e8915efb
    :realsig: (const QString&) const
    :digest: 6d97d5164a270f560e2ab6fa245fe4ff

Returns an uppercase copy of *str*.

If Qt Core is using the ICU libraries, they will be used to perform the transformation according to the rules of the current locale. Otherwise the conversion may be done in a platform-dependent manner, with QString::toUpper() as a generic fallback.

**Note:** In some cases the uppercase form of a string may be longer than the original.

.. seealso:: QString::toUpper().
