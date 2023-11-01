:orphan:

.. sip:class:: PyQt6.QtCore.QTextBoundaryFinder
    :description: QtCore/QTextBoundaryFinder-c.rst

    .. sip:enum:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason
        :description: QtCore/QTextBoundaryFinder-BoundaryReason-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason.BreakOpportunity
            :description: QtCore/QTextBoundaryFinder-BoundaryReason-BreakOpportunity-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason.EndOfItem
            :description: QtCore/QTextBoundaryFinder-BoundaryReason-EndOfItem-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason.MandatoryBreak
            :description: QtCore/QTextBoundaryFinder-BoundaryReason-MandatoryBreak-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason.NotAtBoundary
            :description: QtCore/QTextBoundaryFinder-BoundaryReason-NotAtBoundary-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason.SoftHyphen
            :description: QtCore/QTextBoundaryFinder-BoundaryReason-SoftHyphen-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason.StartOfItem
            :description: QtCore/QTextBoundaryFinder-BoundaryReason-StartOfItem-v.rst

    .. sip:enum:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryType
        :description: QtCore/QTextBoundaryFinder-BoundaryType-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryType.Grapheme
            :description: QtCore/QTextBoundaryFinder-BoundaryType-Grapheme-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryType.Line
            :description: QtCore/QTextBoundaryFinder-BoundaryType-Line-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryType.Sentence
            :description: QtCore/QTextBoundaryFinder-BoundaryType-Sentence-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextBoundaryFinder.BoundaryType.Word
            :description: QtCore/QTextBoundaryFinder-BoundaryType-Word-v.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.__init__
        :description: QtCore/QTextBoundaryFinder-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextBoundaryFinder`
        :description: QtCore/QTextBoundaryFinder-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextBoundaryFinder.BoundaryType`
            Optional[str]
        :description: QtCore/QTextBoundaryFinder-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.boundaryReasons
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextBoundaryFinder.BoundaryReason`
        :description: QtCore/QTextBoundaryFinder-boundaryReasons-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.isAtBoundary
        :returns:
            bool
        :description: QtCore/QTextBoundaryFinder-isAtBoundary-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.isValid
        :returns:
            bool
        :description: QtCore/QTextBoundaryFinder-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.position
        :returns:
            int
        :description: QtCore/QTextBoundaryFinder-position-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.setPosition
        :args:
            int
        :description: QtCore/QTextBoundaryFinder-setPosition-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.string
        :returns:
            str
        :description: QtCore/QTextBoundaryFinder-string-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.toEnd
        :description: QtCore/QTextBoundaryFinder-toEnd-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.toNextBoundary
        :returns:
            int
        :description: QtCore/QTextBoundaryFinder-toNextBoundary-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.toPreviousBoundary
        :returns:
            int
        :description: QtCore/QTextBoundaryFinder-toPreviousBoundary-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.toStart
        :description: QtCore/QTextBoundaryFinder-toStart-f.rst

    .. sip:method:: PyQt6.QtCore.QTextBoundaryFinder.type
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextBoundaryFinder.BoundaryType`
        :description: QtCore/QTextBoundaryFinder-type-f.rst
