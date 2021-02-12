.. sip:enum-description::
    :status: todo
    :digest: 477c19e5161230ad952d5b17cb7ddeb6

This enum type specifies the storage format used by :sip:ref:`~PyQt6.QtCore.QSettings`.

On Unix,  and  mean the same thing, except that the file extension is different (``.conf`` for , ``.ini`` for ).

The INI file format is a Windows file format that Qt supports on all platforms. In the absence of an INI standard, we try to follow what Microsoft does, with the following exceptions:

* If you store types that `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ can't convert to QString (e.g., :sip:ref:`~PyQt6.QtCore.QPoint`, :sip:ref:`~PyQt6.QtCore.QRect`, and :sip:ref:`~PyQt6.QtCore.QSize`), Qt uses an ``@``-based syntax to encode the type. For example:

  .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
      :lines: 106-106

  To minimize compatibility issues, any ``@`` that doesn't appear at the first position in the value or that isn't followed by a Qt type (``Point``, ``Rect``, ``Size``, etc.) is treated as a normal character.

* Although backslash is a special character in INI files, most Windows applications don't escape backslashes (``\``) in file paths:

  .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
      :lines: 111-111

  :sip:ref:`~PyQt6.QtCore.QSettings` always treats backslash as a special character and provides no API for reading or writing such entries.

* The INI file format has severe restrictions on the syntax of a key. Qt works around this by using ``%`` as an escape character in keys. In addition, if you save a top-level setting (a key with no slashes in it, e.g., "someKey"), it will appear in the INI file's "General" section. To avoid overwriting other keys, if you save something using a key such as "General/someKey", the key will be located in the "%General" section, *not* in the "General" section.

* In line with most implementations today, :sip:ref:`~PyQt6.QtCore.QSettings` will assume the INI file is utf-8 encoded. This means that keys and values will be decoded as utf-8 encoded entries and written back as utf-8.

Compatibility with older Qt versions
....................................

Please note that this behavior is different to how :sip:ref:`~PyQt6.QtCore.QSettings` behaved in versions of Qt prior to Qt 6. INI files written with Qt 5 or earlier aree however fully readable by a Qt 6 based application (unless a ini codec different from utf8 had been set). But INI files written with Qt 6 will only be readable by older Qt versions if you set the "iniCodec" to a utf-8 textcodec.

.. seealso:: registerFormat(), :sip:ref:`~PyQt6.QtCore.QSettings.setPath`.
