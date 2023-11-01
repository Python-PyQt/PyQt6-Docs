.. sip:method-description::
    :status: todo
    :pysig: 2e1e4fde32fc7292dbe8e18ea768734a
    :realsig: (const QStringList&)
    :digest: b95ae07b13926972747d4772fcaf760b

Sets the current list of *languages* for the spell checker. Each language should match the name of the ``.bdic`` dictionary. For example, the language ``en-US`` will load the ``en-US.bdic`` dictionary file.

See the `Spellchecker feature documentation <https://doc.qt.io/qt-6/qtwebengine-features.html#spellchecker>`_ for how dictionary files are searched.

For more information about how to compile ``.bdic`` dictionaries, see the `Spellchecker Example <https://doc.qt.io/qt-6/qtwebengine-webenginewidgets-spellchecker-example.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.spellCheckLanguages`.
