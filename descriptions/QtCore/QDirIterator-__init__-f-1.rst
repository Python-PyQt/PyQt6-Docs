.. sip:method-description::
    :status: todo
    :pysig: dc9424db93040988ff6da34b23189de2
    :realsig: (const QString&,QDirIterator::IteratorFlags)
    :digest: 912d22045f3dd847e22203a40434a166

Constructs a :sip:ref:`~PyQt6.QtCore.QDirIterator` that can iterate over *path*. You can pass options via *flags* to decide how the directory should be iterated.

By default, *flags* is :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.NoIteratorFlags`, which provides the same behavior as in :sip:ref:`~PyQt6.QtCore.QDir.entryList`.

**Note:** To list symlinks that point to non existing files, :sip:ref:`~PyQt6.QtCore.QDir.Filters.System` must be passed to the flags.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.next`, IteratorFlags.
