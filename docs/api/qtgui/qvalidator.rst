:orphan:

.. sip:class:: PyQt6.QtGui.QValidator
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QValidator-c.rst

    .. sip:enum:: PyQt6.QtGui.QValidator.State
        :description: QtGui/QValidator-State-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QValidator.State.Acceptable
            :description: QtGui/QValidator-State-Acceptable-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QValidator.State.Intermediate
            :description: QtGui/QValidator-State-Intermediate-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QValidator.State.Invalid
            :description: QtGui/QValidator-State-Invalid-v.rst

    .. sip:method:: PyQt6.QtGui.QValidator.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QValidator-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QValidator.fixup
        :args:
            Optional[str]
        :returns:
            str
        :description: QtGui/QValidator-fixup-f-1.rst

    .. sip:method:: PyQt6.QtGui.QValidator.locale
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtGui/QValidator-locale-f.rst

    .. sip:method:: PyQt6.QtGui.QValidator.setLocale
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtGui/QValidator-setLocale-f.rst

    .. sip:method:: PyQt6.QtGui.QValidator.validate
        :args:
            Optional[str]
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QValidator.State`
            str
            int
        :description: QtGui/QValidator-validate-f-1.rst

    .. sip:signal:: PyQt6.QtGui.QValidator.changed
        :description: QtGui/QValidator-changed-s.rst
