.. sip:method-description::
    :status: todo
    :pysig: 65e5a775760860a64bb6636225fb5cff
    :realsig: (const QString&,const QStringList&,QDir::Filters,QDirIterator::IteratorFlags)
    :digest: 225bbe3f8dd1e9a8ec03adf5c6747798

Constructs a :sip:ref:`~PyQt6.QtCore.QDirIterator` that can iterate over *path*, using *nameFilters* and *filters*. You can pass options via *flags* to decide how the directory should be iterated.

By default, *flags* is :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags`, which provides the same behavior as :sip:ref:`~PyQt6.QtCore.QDir.entryList`.

For example, the following iterator could be used to iterate over audio files:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdiriterator.py
    :lines: 76-76

**Note:** To list symlinks that point to non existing files, :sip:ref:`~PyQt6.QtCore.QDir.Filter.System` must be passed to the flags.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.next`, IteratorFlags, :sip:ref:`~PyQt6.QtCore.QDir.setNameFilters`.
