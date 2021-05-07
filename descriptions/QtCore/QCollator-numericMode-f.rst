.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ed48706246613cbd5bebc28dbbc025ba

Returns ``true`` if numeric sorting is enabled, ``false`` otherwise.

When ``true``, numerals are recognized as numbers and sorted in arithmetic order; for example, 100 sortes after 99. When ``false``, numbers are sorted in lexical order, so that 100 sorts before 99 (because 1 is before 9). By default, this option is disabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCollator.setNumericMode`.
