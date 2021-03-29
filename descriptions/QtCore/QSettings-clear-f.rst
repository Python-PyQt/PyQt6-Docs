.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f60b345138ac4e869087c14d6e533385

Removes all entries in the primary location associated to this :sip:ref:`~PyQt6.QtCore.QSettings` object.

Entries in fallback locations are not removed.

If you only want to remove the entries in the current :sip:ref:`~PyQt6.QtCore.QSettings.group`, use remove("") instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.remove`, :sip:ref:`~PyQt6.QtCore.QSettings.setFallbacksEnabled`.
