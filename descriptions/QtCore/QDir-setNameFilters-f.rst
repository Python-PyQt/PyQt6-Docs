.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 73a05017b6bbeea0a6e42c88d0069632

Sets the name filters used by :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList` to the list of filters specified by *nameFilters*.

Each name filter is a wildcard (globbing) filter that understands ``\*`` and ``?`` wildcards. See :sip:ref:`~PyQt6.QtCore.QRegularExpression` Wildcard Matching.

For example, the following code sets three name filters on a :sip:ref:`~PyQt6.QtCore.QDir` to ensure that only files with extensions typically used for C++ source files are listed:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qdir-namefilters-main.py
    :lines: 63-65

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.nameFilters`, :sip:ref:`~PyQt6.QtCore.QDir.setFilter`.
