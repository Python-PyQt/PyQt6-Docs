:orphan:

.. sip:class:: PyQt6.QtGui.QInputMethodEvent
    :inherits: :sip:ref:`~PyQt6.QtCore.QEvent`
    :description: QtGui/QInputMethodEvent-c.rst

    .. sip:enum:: PyQt6.QtGui.QInputMethodEvent.AttributeType
        :description: QtGui/QInputMethodEvent-AttributeType-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputMethodEvent.AttributeType.Cursor
            :description: QtGui/QInputMethodEvent-AttributeType-Cursor-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputMethodEvent.AttributeType.Language
            :description: QtGui/QInputMethodEvent-AttributeType-Language-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputMethodEvent.AttributeType.Ruby
            :description: QtGui/QInputMethodEvent-AttributeType-Ruby-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputMethodEvent.AttributeType.Selection
            :description: QtGui/QInputMethodEvent-AttributeType-Selection-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputMethodEvent.AttributeType.TextFormat
            :description: QtGui/QInputMethodEvent-AttributeType-TextFormat-v.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.__init__
        :description: QtGui/QInputMethodEvent-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.__init__
        :args:
            Optional[str]
            Iterable[:sip:ref:`~PyQt6.QtGui.QInputMethodEvent.Attribute`]
        :description: QtGui/QInputMethodEvent-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.attributes
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QInputMethodEvent.Attribute`]
        :description: QtGui/QInputMethodEvent-attributes-f-1.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.clone
        :returns:
            :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`
        :description: QtGui/QInputMethodEvent-clone-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.commitString
        :returns:
            str
        :description: QtGui/QInputMethodEvent-commitString-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.preeditString
        :returns:
            str
        :description: QtGui/QInputMethodEvent-preeditString-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.replacementLength
        :returns:
            int
        :description: QtGui/QInputMethodEvent-replacementLength-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.replacementStart
        :returns:
            int
        :description: QtGui/QInputMethodEvent-replacementStart-f.rst

    .. sip:method:: PyQt6.QtGui.QInputMethodEvent.setCommitString
        :args:
            Optional[str]
            from: int = 0
            length: int = 0
        :description: QtGui/QInputMethodEvent-setCommitString-f-1.rst
