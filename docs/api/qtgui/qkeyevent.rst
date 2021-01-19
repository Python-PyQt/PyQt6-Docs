:orphan:

.. sip:class:: PyQt6.QtGui.QKeyEvent
    :inherits: :sip:ref:`~PyQt6.QtGui.QInputEvent`
    :description: QtGui/QKeyEvent-c.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent.Type`
            int
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers`
            text: str = ''
            autorep: bool = False
            count: int = 1
        :description: QtGui/QKeyEvent-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent.Type`
            int
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers`
            int
            int
            int
            text: str = ''
            autorep: bool = False
            count: int = 1
            device: :sip:ref:`~PyQt6.QtGui.QInputDevice` = QInputDevice.primaryKeyboard()
        :description: QtGui/QKeyEvent-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.clone
        :returns:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtGui/QKeyEvent-clone-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.count
        :returns:
            int
        :description: QtGui/QKeyEvent-count-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`
        :returns:
            bool
        :description: QtGui/QKeyEvent-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.isAutoRepeat
        :returns:
            bool
        :description: QtGui/QKeyEvent-isAutoRepeat-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.key
        :returns:
            int
        :description: QtGui/QKeyEvent-key-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.keyCombination
        :returns:
            :sip:ref:`~PyQt6.QtCore.QKeyCombination`
        :description: QtGui/QKeyEvent-keyCombination-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.__len__
        :returns:
            int
        :description: QtGui/QKeyEvent-__len__-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.matches
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`
        :returns:
            bool
        :description: QtGui/QKeyEvent-matches-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.modifiers
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers`
        :description: QtGui/QKeyEvent-modifiers-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.nativeModifiers
        :returns:
            int
        :description: QtGui/QKeyEvent-nativeModifiers-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.nativeScanCode
        :returns:
            int
        :description: QtGui/QKeyEvent-nativeScanCode-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.nativeVirtualKey
        :returns:
            int
        :description: QtGui/QKeyEvent-nativeVirtualKey-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`
        :returns:
            bool
        :description: QtGui/QKeyEvent-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QKeyEvent.text
        :returns:
            str
        :description: QtGui/QKeyEvent-text-f.rst
