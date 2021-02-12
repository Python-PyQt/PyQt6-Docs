.. sip:method-description::
    :status: todo
    :pysig: 61c2636f9a4e2f4f51a8e0763c14f2ba
    :realsig: (const QDir&,QDirIterator::IteratorFlags)
    :digest: 0956bfcc99a52b007370e586c7885e9e

Constructs a :sip:ref:`~PyQt6.QtCore.QDirIterator` that can iterate over *dir*'s entrylist, using *dir*'s name filters and regular filters. You can pass options via *flags* to decide how the directory should be iterated.

By default, *flags* is :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags`, which provides the same behavior as in :sip:ref:`~PyQt6.QtCore.QDir.entryList`.

The sorting in *dir* is ignored.

**Note:** To list symlinks that point to non existing files, :sip:ref:`~PyQt6.QtCore.QDir.Filters.System` must be passed to the flags.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.next`, IteratorFlags.
