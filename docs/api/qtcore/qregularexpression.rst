:orphan:

.. sip:class:: PyQt6.QtCore.QRegularExpression
    :description: QtCore/QRegularExpression-c.rst

    .. sip:enum:: PyQt6.QtCore.QRegularExpression.MatchOptions
        :description: QtCore/QRegularExpression-MatchOptions-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchOptions.AnchorAtOffsetMatchOption
            :description: QtCore/QRegularExpression-MatchOptions-AnchorAtOffsetMatchOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchOptions.DontCheckSubjectStringMatchOption
            :description: QtCore/QRegularExpression-MatchOptions-DontCheckSubjectStringMatchOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchOptions.NoMatchOption
            :description: QtCore/QRegularExpression-MatchOptions-NoMatchOption-v.rst

    .. sip:enum:: PyQt6.QtCore.QRegularExpression.MatchType
        :description: QtCore/QRegularExpression-MatchType-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchType.NoMatch
            :description: QtCore/QRegularExpression-MatchType-NoMatch-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchType.NormalMatch
            :description: QtCore/QRegularExpression-MatchType-NormalMatch-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchType.PartialPreferCompleteMatch
            :description: QtCore/QRegularExpression-MatchType-PartialPreferCompleteMatch-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchType.PartialPreferFirstMatch
            :description: QtCore/QRegularExpression-MatchType-PartialPreferFirstMatch-v.rst

    .. sip:enum:: PyQt6.QtCore.QRegularExpression.PatternOptions
        :description: QtCore/QRegularExpression-PatternOptions-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.CaseInsensitiveOption
            :description: QtCore/QRegularExpression-PatternOptions-CaseInsensitiveOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.DontCaptureOption
            :description: QtCore/QRegularExpression-PatternOptions-DontCaptureOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.DotMatchesEverythingOption
            :description: QtCore/QRegularExpression-PatternOptions-DotMatchesEverythingOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.ExtendedPatternSyntaxOption
            :description: QtCore/QRegularExpression-PatternOptions-ExtendedPatternSyntaxOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.InvertedGreedinessOption
            :description: QtCore/QRegularExpression-PatternOptions-InvertedGreedinessOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.MultilineOption
            :description: QtCore/QRegularExpression-PatternOptions-MultilineOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.NoPatternOption
            :description: QtCore/QRegularExpression-PatternOptions-NoPatternOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOptions.UseUnicodePropertiesOption
            :description: QtCore/QRegularExpression-PatternOptions-UseUnicodePropertiesOption-v.rst

    .. sip:enum:: PyQt6.QtCore.QRegularExpression.WildcardConversionOptions
        :description: QtCore/QRegularExpression-WildcardConversionOptions-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.WildcardConversionOptions.DefaultWildcardConversion
            :description: QtCore/QRegularExpression-WildcardConversionOptions-DefaultWildcardConversion-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.WildcardConversionOptions.UnanchoredWildcardConversion
            :description: QtCore/QRegularExpression-WildcardConversionOptions-UnanchoredWildcardConversion-v.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__init__
        :description: QtCore/QRegularExpression-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :description: QtCore/QRegularExpression-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__init__
        :args:
            str
            options: :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOptions` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOptions.NoPatternOption`
        :description: QtCore/QRegularExpression-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.anchoredPattern
        :args:
            str
        :returns:
            str
        :static:
        :description: QtCore/QRegularExpression-anchoredPattern-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.captureCount
        :returns:
            int
        :description: QtCore/QRegularExpression-captureCount-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__eq__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :returns:
            bool
        :description: QtCore/QRegularExpression-__eq__-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.errorString
        :returns:
            str
        :description: QtCore/QRegularExpression-errorString-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.escape
        :args:
            str
        :returns:
            str
        :static:
        :description: QtCore/QRegularExpression-escape-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.fromWildcard
        :args:
            str
            cs: :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity` = :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity.CaseInsensitive`
            options: :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOptions` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOptions.DefaultWildcardConversion`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :static:
        :description: QtCore/QRegularExpression-fromWildcard-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.globalMatch
        :args:
            str
            offset: int = 0
            matchType: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType.NormalMatch`
            matchOptions: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOptions` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOptions.NoMatchOption`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator`
        :description: QtCore/QRegularExpression-globalMatch-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__hash__
        :returns:
            int
        :description: QtCore/QRegularExpression-__hash__-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.isValid
        :returns:
            bool
        :description: QtCore/QRegularExpression-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.match
        :args:
            str
            offset: int = 0
            matchType: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType.NormalMatch`
            matchOptions: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOptions` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOptions.NoMatchOption`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch`
        :description: QtCore/QRegularExpression-match-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.namedCaptureGroups
        :returns:
            List[str]
        :description: QtCore/QRegularExpression-namedCaptureGroups-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__ne__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :returns:
            bool
        :description: QtCore/QRegularExpression-__ne__-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.optimize
        :description: QtCore/QRegularExpression-optimize-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.pattern
        :returns:
            str
        :description: QtCore/QRegularExpression-pattern-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.patternErrorOffset
        :returns:
            int
        :description: QtCore/QRegularExpression-patternErrorOffset-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.patternOptions
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOptions`
        :description: QtCore/QRegularExpression-patternOptions-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__repr__
        :returns:
            str
        :description: QtCore/QRegularExpression-__repr__-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.setPattern
        :args:
            str
        :description: QtCore/QRegularExpression-setPattern-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.setPatternOptions
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOptions`
        :description: QtCore/QRegularExpression-setPatternOptions-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :description: QtCore/QRegularExpression-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.wildcardToRegularExpression
        :args:
            str
            options: :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOptions` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOptions.DefaultWildcardConversion`
        :returns:
            str
        :static:
        :description: QtCore/QRegularExpression-wildcardToRegularExpression-f.rst
