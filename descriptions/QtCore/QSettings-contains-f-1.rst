.. sip:method-description::
    :status: todo
    :pysig: 386dec0d13ec1078829385dedf2f9960
    :realsig: (QAnyStringView) const
    :digest: 8aff9be0d59c2006fd70e56fe13b2836

Returns ``true`` if there exists a setting called *key*; returns false otherwise.

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, *key* is taken to be relative to that group.

Note that the Windows registry and INI files use case-insensitive keys, whereas the CFPreferences API on macOS and iOS uses case-sensitive keys. To avoid portability problems, see the :ref:`qsettings-section-and-key-syntax` rules.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.value`, :sip:ref:`~PyQt6.QtCore.QSettings.setValue`.
