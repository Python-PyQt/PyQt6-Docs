.. sip:method-description::
    :status: todo
    :pysig: 469c3d5de45760d2e753a158b05ea5cb
    :realsig: (QAnyStringView) const
    :digest: ba8f0c6338408a3f56e837653595ec91

Returns ``true`` if there exists a setting called *key*; returns false otherwise.

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, *key* is taken to be relative to that group.

Key lookup will either be sensitive or insensitive to case depending on file format and operating system. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.setValue`.
