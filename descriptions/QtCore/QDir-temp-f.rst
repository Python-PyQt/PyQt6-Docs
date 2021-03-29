.. sip:method-description::
    :status: todo
    :pysig: 5c3fbdcc7780f81e902e684b72bd8429
    :realsig: ()
    :digest: ac6b52ee301176268d58bd9095ef34f7

Returns the system's temporary directory.

The directory is constructed using the absolute canonical path of the temporary directory, ensuring that its :sip:ref:`~PyQt6.QtCore.QDir.path` will be the same as its :sip:ref:`~PyQt6.QtCore.QDir.absolutePath`.

See :sip:ref:`~PyQt6.QtCore.QDir.tempPath` for details.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.drives`, :sip:ref:`~PyQt6.QtCore.QDir.current`, :sip:ref:`~PyQt6.QtCore.QDir.home`, :sip:ref:`~PyQt6.QtCore.QDir.root`.
