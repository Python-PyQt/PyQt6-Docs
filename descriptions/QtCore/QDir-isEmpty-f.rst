.. sip:method-description::
    :status: todo
    :pysig: 81af2a9124f2d0b1b3050186b39fb7b0
    :realsig: (QDir::Filters) const
    :digest: 8300a24df1da100e54986b588d192994

Returns whether the directory is empty.

Equivalent to ``count() == 0`` with filters ``QDir::AllEntries | QDir::NoDotAndDotDot``, but faster as it just checks whether the directory contains at least one entry.

**Note:** Unless you set the *filters* flags to include ``QDir::NoDotAndDotDot`` (as the default value does), no directory is empty.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.count`, :sip:ref:`~PyQt6.QtCore.QDir.entryList`, :sip:ref:`~PyQt6.QtCore.QDir.setFilter`.
