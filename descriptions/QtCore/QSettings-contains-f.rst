.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: f490825b634d5b2d16bedd235b08c103

Returns ``true`` if there exists a setting called *key*; returns false otherwise.

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, *key* is taken to be relative to that group.

Note that the Windows registry and INI files use case-insensitive keys, whereas the CFPreferences API on macOS and iOS uses case-sensitive keys. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.setValue`.
