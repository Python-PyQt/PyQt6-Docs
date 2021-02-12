.. sip:method-description::
    :status: todo
    :pysig: 72c3a830a38829ac9ab9c29295c900cd
    :realsig: (const QString&,QDir::Filters,QDirIterator::IteratorFlags)
    :digest: 3ec1924022917a0966ac01aaf0bad2f7

Constructs a :sip:ref:`~PyQt6.QtCore.QDirIterator` that can iterate over *path*, with no name filtering and *filters* for entry filtering. You can pass options via *flags* to decide how the directory should be iterated.

By default, *filters* is :sip:ref:`~PyQt6.QtCore.QDir.Filters.NoFilter`, and *flags* is :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags`, which provides the same behavior as in :sip:ref:`~PyQt6.QtCore.QDir.entryList`.

**Note:** To list symlinks that point to non existing files, :sip:ref:`~PyQt6.QtCore.QDir.Filters.System` must be passed to the flags.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.next`, IteratorFlags.
