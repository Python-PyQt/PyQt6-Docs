:orphan:

.. sip:class:: PyQt6.QtCore.QTranslator
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QTranslator-c.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QTranslator-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.filePath
        :returns:
            str
        :description: QtCore/QTranslator-filePath-f.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.isEmpty
        :returns:
            bool
        :description: QtCore/QTranslator-isEmpty-f.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.language
        :returns:
            str
        :description: QtCore/QTranslator-language-f.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.load
        :args:
            str|None
            directory: str|None = ''
            searchDelimiters: str|None = ''
            suffix: str|None = ''
        :returns:
            bool
        :description: QtCore/QTranslator-load-f.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.load
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
            str|None
            prefix: str|None = ''
            directory: str|None = ''
            suffix: str|None = ''
        :returns:
            bool
        :description: QtCore/QTranslator-load-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.loadFromData
        :args:
            bytes
            directory: str|None = ''
        :returns:
            bool
        :description: QtCore/QTranslator-loadFromData-f.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.translate
        :args:
            str
            str
            disambiguation: str = None
            n: int = -1
        :returns:
            str
        :description: QtCore/QTranslator-translate-f.rst
