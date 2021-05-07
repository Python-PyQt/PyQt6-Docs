.. sip:method-description::
    :status: todo
    :pysig: ae80ec5691f8ed2dc0468e4d43b9d5ba
    :realsig: (const QDir&,QDirIterator::IteratorFlags)
    :digest: 0956bfcc99a52b007370e586c7885e9e

Constructs a :sip:ref:`~PyQt6.QtCore.QDirIterator` that can iterate over *dir*'s entrylist, using *dir*'s name filters and regular filters. You can pass options via *flags* to decide how the directory should be iterated.

By default, *flags* is :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags`, which provides the same behavior as in :sip:ref:`~PyQt6.QtCore.QDir.entryList`.

The sorting in *dir* is ignored.

**Note:** To list symlinks that point to non existing files, :sip:ref:`~PyQt6.QtCore.QDir.Filter.System` must be passed to the flags.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.next`, IteratorFlags.
