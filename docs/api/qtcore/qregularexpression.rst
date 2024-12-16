:orphan:

.. sip:class:: PyQt6.QtCore.QRegularExpression
    :description: QtCore/QRegularExpression-c.rst

    .. sip:enum:: PyQt6.QtCore.QRegularExpression.MatchOption
        :description: QtCore/QRegularExpression-MatchOption-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchOption.AnchorAtOffsetMatchOption
            :description: QtCore/QRegularExpression-MatchOption-AnchorAtOffsetMatchOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchOption.DontCheckSubjectStringMatchOption
            :description: QtCore/QRegularExpression-MatchOption-DontCheckSubjectStringMatchOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.MatchOption.NoMatchOption
            :description: QtCore/QRegularExpression-MatchOption-NoMatchOption-v.rst

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

    .. sip:enum:: PyQt6.QtCore.QRegularExpression.PatternOption
        :description: QtCore/QRegularExpression-PatternOption-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.CaseInsensitiveOption
            :description: QtCore/QRegularExpression-PatternOption-CaseInsensitiveOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.DontCaptureOption
            :description: QtCore/QRegularExpression-PatternOption-DontCaptureOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.DotMatchesEverythingOption
            :description: QtCore/QRegularExpression-PatternOption-DotMatchesEverythingOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.ExtendedPatternSyntaxOption
            :description: QtCore/QRegularExpression-PatternOption-ExtendedPatternSyntaxOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.InvertedGreedinessOption
            :description: QtCore/QRegularExpression-PatternOption-InvertedGreedinessOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.MultilineOption
            :description: QtCore/QRegularExpression-PatternOption-MultilineOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.NoPatternOption
            :description: QtCore/QRegularExpression-PatternOption-NoPatternOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.PatternOption.UseUnicodePropertiesOption
            :description: QtCore/QRegularExpression-PatternOption-UseUnicodePropertiesOption-v.rst

    .. sip:enum:: PyQt6.QtCore.QRegularExpression.WildcardConversionOption
        :description: QtCore/QRegularExpression-WildcardConversionOption-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.WildcardConversionOption.DefaultWildcardConversion
            :description: QtCore/QRegularExpression-WildcardConversionOption-DefaultWildcardConversion-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.WildcardConversionOption.NonPathWildcardConversion
            :description: QtCore/QRegularExpression-WildcardConversionOption-NonPathWildcardConversion-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QRegularExpression.WildcardConversionOption.UnanchoredWildcardConversion
            :description: QtCore/QRegularExpression-WildcardConversionOption-UnanchoredWildcardConversion-v.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__init__
        :description: QtCore/QRegularExpression-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :description: QtCore/QRegularExpression-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__init__
        :args:
            Optional[str]
            options: :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOption` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOption.NoPatternOption`
        :description: QtCore/QRegularExpression-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.anchoredPattern
        :args:
            Optional[str]
        :returns:
            str
        :static:
        :description: QtCore/QRegularExpression-anchoredPattern-f-1.rst

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
            Optional[str]
        :returns:
            str
        :static:
        :description: QtCore/QRegularExpression-escape-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.fromWildcard
        :args:
            str
            cs: :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity` = :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity.CaseInsensitive`
            options: :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOption` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOption.DefaultWildcardConversion`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :static:
        :description: QtCore/QRegularExpression-fromWildcard-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.globalMatch
        :args:
            Optional[str]
            offset: int = 0
            matchType: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType.NormalMatch`
            matchOptions: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption.NoMatchOption`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator`
        :description: QtCore/QRegularExpression-globalMatch-f-2.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.globalMatchView
        :args:
            str
            offset: int = 0
            matchType: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType.NormalMatch`
            matchOptions: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption.NoMatchOption`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatchIterator`
        :description: QtCore/QRegularExpression-globalMatchView-f.rst

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
            Optional[str]
            offset: int = 0
            matchType: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType.NormalMatch`
            matchOptions: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption.NoMatchOption`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch`
        :description: QtCore/QRegularExpression-match-f-2.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.matchView
        :args:
            str
            offset: int = 0
            matchType: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType.NormalMatch`
            matchOptions: :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchOption.NoMatchOption`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch`
        :description: QtCore/QRegularExpression-matchView-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.namedCaptureGroups
        :returns:
            list[str]
        :description: QtCore/QRegularExpression-namedCaptureGroups-f-1.rst

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
            :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOption`
        :description: QtCore/QRegularExpression-patternOptions-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.__repr__
        :returns:
            str
        :description: QtCore/QRegularExpression-__repr__-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.setPattern
        :args:
            Optional[str]
        :description: QtCore/QRegularExpression-setPattern-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.setPatternOptions
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression.PatternOption`
        :description: QtCore/QRegularExpression-setPatternOptions-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :description: QtCore/QRegularExpression-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QRegularExpression.wildcardToRegularExpression
        :args:
            str
            options: :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOption` = :sip:ref:`~PyQt6.QtCore.QRegularExpression.WildcardConversionOption.DefaultWildcardConversion`
        :returns:
            str
        :static:
        :description: QtCore/QRegularExpression-wildcardToRegularExpression-f-1.rst
