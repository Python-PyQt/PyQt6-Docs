:orphan:

.. sip:class:: PyQt6.QtCore.QCommandLineParser
    :description: QtCore/QCommandLineParser-c.rst

    .. sip:enum:: PyQt6.QtCore.QCommandLineParser.MessageType
        :description: QtCore/QCommandLineParser-MessageType-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QCommandLineParser.MessageType.Error
            :description: QtCore/QCommandLineParser-MessageType-Error-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCommandLineParser.MessageType.Information
            :description: QtCore/QCommandLineParser-MessageType-Information-v.rst

    .. sip:enum:: PyQt6.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode
        :description: QtCore/QCommandLineParser-OptionsAfterPositionalArgumentsMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode.ParseAsOptions
            :description: QtCore/QCommandLineParser-OptionsAfterPositionalArgumentsMode-ParseAsOptions-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode.ParseAsPositionalArguments
            :description: QtCore/QCommandLineParser-OptionsAfterPositionalArgumentsMode-ParseAsPositionalArguments-v.rst

    .. sip:enum:: PyQt6.QtCore.QCommandLineParser.SingleDashWordOptionMode
        :description: QtCore/QCommandLineParser-SingleDashWordOptionMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QCommandLineParser.SingleDashWordOptionMode.ParseAsCompactedShortOptions
            :description: QtCore/QCommandLineParser-SingleDashWordOptionMode-ParseAsCompactedShortOptions-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCommandLineParser.SingleDashWordOptionMode.ParseAsLongOptions
            :description: QtCore/QCommandLineParser-SingleDashWordOptionMode-ParseAsLongOptions-v.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.__init__
        :description: QtCore/QCommandLineParser-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.addHelpOption
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCommandLineOption`
        :description: QtCore/QCommandLineParser-addHelpOption-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.addOption
        :args:
            :sip:ref:`~PyQt6.QtCore.QCommandLineOption`
        :returns:
            bool
        :description: QtCore/QCommandLineParser-addOption-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.addOptions
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QCommandLineOption`]
        :returns:
            bool
        :description: QtCore/QCommandLineParser-addOptions-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.addPositionalArgument
        :args:
            Optional[str]
            Optional[str]
            syntax: Optional[str] = ''
        :description: QtCore/QCommandLineParser-addPositionalArgument-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.addVersionOption
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCommandLineOption`
        :description: QtCore/QCommandLineParser-addVersionOption-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.applicationDescription
        :returns:
            str
        :description: QtCore/QCommandLineParser-applicationDescription-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.clearPositionalArguments
        :description: QtCore/QCommandLineParser-clearPositionalArguments-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.errorText
        :returns:
            str
        :description: QtCore/QCommandLineParser-errorText-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.helpText
        :returns:
            str
        :description: QtCore/QCommandLineParser-helpText-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.isSet
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtCore/QCommandLineParser-isSet-f-2.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.isSet
        :args:
            :sip:ref:`~PyQt6.QtCore.QCommandLineOption`
        :returns:
            bool
        :description: QtCore/QCommandLineParser-isSet-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.optionNames
        :returns:
            list[str]
        :description: QtCore/QCommandLineParser-optionNames-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.parse
        :args:
            Iterable[Optional[str]]
        :returns:
            bool
        :description: QtCore/QCommandLineParser-parse-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.positionalArguments
        :returns:
            list[str]
        :description: QtCore/QCommandLineParser-positionalArguments-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.process
        :args:
            Iterable[Optional[str]]
        :description: QtCore/QCommandLineParser-process-f-2.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.process
        :args:
            :sip:ref:`~PyQt6.QtCore.QCoreApplication`
        :description: QtCore/QCommandLineParser-process-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.setApplicationDescription
        :args:
            Optional[str]
        :description: QtCore/QCommandLineParser-setApplicationDescription-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.setOptionsAfterPositionalArgumentsMode
        :args:
            :sip:ref:`~PyQt6.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode`
        :description: QtCore/QCommandLineParser-setOptionsAfterPositionalArgumentsMode-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.setSingleDashWordOptionMode
        :args:
            :sip:ref:`~PyQt6.QtCore.QCommandLineParser.SingleDashWordOptionMode`
        :description: QtCore/QCommandLineParser-setSingleDashWordOptionMode-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.showHelp
        :args:
            exitCode: int = 0
        :description: QtCore/QCommandLineParser-showHelp-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.showMessageAndExit
        :args:
            :sip:ref:`~PyQt6.QtCore.QCommandLineParser.MessageType`
            Optional[str]
            exitCode: int = 0
        :static:
        :description: QtCore/QCommandLineParser-showMessageAndExit-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.showVersion
        :description: QtCore/QCommandLineParser-showVersion-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.unknownOptionNames
        :returns:
            list[str]
        :description: QtCore/QCommandLineParser-unknownOptionNames-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.value
        :args:
            Optional[str]
        :returns:
            str
        :description: QtCore/QCommandLineParser-value-f-2.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.value
        :args:
            :sip:ref:`~PyQt6.QtCore.QCommandLineOption`
        :returns:
            str
        :description: QtCore/QCommandLineParser-value-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.values
        :args:
            Optional[str]
        :returns:
            list[str]
        :description: QtCore/QCommandLineParser-values-f.rst

    .. sip:method:: PyQt6.QtCore.QCommandLineParser.values
        :args:
            :sip:ref:`~PyQt6.QtCore.QCommandLineOption`
        :returns:
            list[str]
        :description: QtCore/QCommandLineParser-values-f-3.rst
