.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: f260726cb3c5b1514a26a25422bdbc3a

Returns ``true`` if settings can be written using this :sip:ref:`~PyQt6.QtCore.QSettings` object; returns ``false`` otherwise.

One reason why isWritable() might return false is if :sip:ref:`~PyQt6.QtCore.QSettings` operates on a read-only file.

**Warning:** This function is not perfectly reliable, because the file permissions can change at any time.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.fileName`, :sip:ref:`~PyQt6.QtCore.QSettings.status`, :sip:ref:`~PyQt6.QtCore.QSettings.sync`.
