.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2670eb1f12449382d6e720c0f050f6ac

Returns ``true`` if the directory is readable *and* we can open files by name; otherwise returns ``false``.

**Warning:** A false value from this function is not a guarantee that files in the directory are not accessible.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isReadable`.
