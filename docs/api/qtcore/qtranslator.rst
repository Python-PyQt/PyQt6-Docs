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
            Optional[str]
            directory: Optional[str] = ''
            searchDelimiters: Optional[str] = ''
            suffix: Optional[str] = ''
        :returns:
            bool
        :description: QtCore/QTranslator-load-f-2.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.load
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
            Optional[str]
            prefix: Optional[str] = ''
            directory: Optional[str] = ''
            suffix: Optional[str] = ''
        :returns:
            bool
        :description: QtCore/QTranslator-load-f-3.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.loadFromData
        :args:
            bytes
            directory: Optional[str] = ''
        :returns:
            bool
        :description: QtCore/QTranslator-loadFromData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTranslator.translate
        :args:
            str
            str
            disambiguation: str = None
            n: int = -1
        :returns:
            str
        :description: QtCore/QTranslator-translate-f.rst
