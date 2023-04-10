.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: fd9d961335e8bab2962bd134ce1bb92a

Returns the total number of directories and files in the directory.

Equivalent to :sip:ref:`~PyQt6.QtCore.QDir.entryList`.count().

**Note:** In Qt versions prior to 6.5, this function returned ``uint``, not ``qsizetype``.

.. seealso:: operator[](), :sip:ref:`~PyQt6.QtCore.QDir.entryList`.
