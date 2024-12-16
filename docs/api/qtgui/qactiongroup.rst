:orphan:

.. sip:class:: PyQt6.QtGui.QActionGroup
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QActionGroup-c.rst

    .. sip:enum:: PyQt6.QtGui.QActionGroup.ExclusionPolicy
        :description: QtGui/QActionGroup-ExclusionPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QActionGroup.ExclusionPolicy.Exclusive
            :description: QtGui/QActionGroup-ExclusionPolicy-Exclusive-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QActionGroup.ExclusionPolicy.ExclusiveOptional
            :description: QtGui/QActionGroup-ExclusionPolicy-ExclusiveOptional-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QActionGroup.ExclusionPolicy.None_
            :description: QtGui/QActionGroup-ExclusionPolicy-None_-v.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtGui/QActionGroup-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.actions
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QAction`]
        :description: QtGui/QActionGroup-actions-f-1.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QActionGroup-addAction-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.addAction
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QActionGroup-addAction-f-3.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QActionGroup-addAction-f-4.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.checkedAction
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QActionGroup-checkedAction-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.exclusionPolicy
        :returns:
            :sip:ref:`~PyQt6.QtGui.QActionGroup.ExclusionPolicy`
        :description: QtGui/QActionGroup-exclusionPolicy-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.isEnabled
        :returns:
            bool
        :description: QtGui/QActionGroup-isEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.isExclusive
        :returns:
            bool
        :description: QtGui/QActionGroup-isExclusive-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.isVisible
        :returns:
            bool
        :description: QtGui/QActionGroup-isVisible-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.removeAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QActionGroup-removeAction-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.setDisabled
        :args:
            bool
        :description: QtGui/QActionGroup-setDisabled-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.setEnabled
        :args:
            bool
        :description: QtGui/QActionGroup-setEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.setExclusionPolicy
        :args:
            :sip:ref:`~PyQt6.QtGui.QActionGroup.ExclusionPolicy`
        :description: QtGui/QActionGroup-setExclusionPolicy-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.setExclusive
        :args:
            bool
        :description: QtGui/QActionGroup-setExclusive-f.rst

    .. sip:method:: PyQt6.QtGui.QActionGroup.setVisible
        :args:
            bool
        :description: QtGui/QActionGroup-setVisible-f.rst

    .. sip:signal:: PyQt6.QtGui.QActionGroup.hovered
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QActionGroup-hovered-s.rst

    .. sip:signal:: PyQt6.QtGui.QActionGroup.triggered
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtGui/QActionGroup-triggered-s.rst
