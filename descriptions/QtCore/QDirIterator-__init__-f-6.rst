.. sip:method-description::
    :status: todo
    :pysig: c83fed937a9dd32c7831a51c2851fb28
    :realsig: (const QString&,QDir::Filters,QDirIterator::IteratorFlags)
    :digest: 3ec1924022917a0966ac01aaf0bad2f7

Constructs a :sip:ref:`~PyQt6.QtCore.QDirIterator` that can iterate over *path*, with no name filtering and *filters* for entry filtering. You can pass options via *flags* to decide how the directory should be iterated.

By default, *filters* is :sip:ref:`~PyQt6.QtCore.QDir.Filter.NoFilter`, and *flags* is :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags`, which provides the same behavior as in :sip:ref:`~PyQt6.QtCore.QDir.entryList`.

**Note:** To list symlinks that point to non existing files, :sip:ref:`~PyQt6.QtCore.QDir.Filter.System` must be passed to the flags.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.next`, IteratorFlags.
