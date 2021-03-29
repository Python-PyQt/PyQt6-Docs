.. sip:method-description::
    :status: todo
    :pysig: e85ccfd342f8b452da34205f48e8f8cb
    :realsig: (const QString&) const
    :digest: e60387eba2dbd309aff2f3bb6f01ef65

Returns a  for *string*.

Creating the sort key is usually somewhat slower, than using the :sip:ref:`~PyQt6.QtCore.QCollator.compare` methods directly. But if the string is compared repeatedly (e.g. when sorting a whole list of strings), it's usually faster to create the sort keys for each string and then sort using the keys.

**Note:** Not supported with the C (a.k.a. POSIX) locale on Darwin.
