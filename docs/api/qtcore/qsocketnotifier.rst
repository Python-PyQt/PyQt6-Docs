:orphan:

.. sip:class:: PyQt6.QtCore.QSocketNotifier
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QSocketNotifier-c.rst

    .. sip:enum:: PyQt6.QtCore.QSocketNotifier.Type
        :description: QtCore/QSocketNotifier-Type-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSocketNotifier.Type.Exception
            :description: QtCore/QSocketNotifier-Type-Exception-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSocketNotifier.Type.Read
            :description: QtCore/QSocketNotifier-Type-Read-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSocketNotifier.Type.Write
            :description: QtCore/QSocketNotifier-Type-Write-v.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSocketNotifier-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.__init__
        :args:
            :py:class:`~PyQt6.sip.voidptr`
            :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSocketNotifier-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QSocketNotifier-event-f.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.isEnabled
        :returns:
            bool
        :description: QtCore/QSocketNotifier-isEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.isValid
        :returns:
            bool
        :description: QtCore/QSocketNotifier-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.setEnabled
        :args:
            bool
        :description: QtCore/QSocketNotifier-setEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.setSocket
        :args:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtCore/QSocketNotifier-setSocket-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.socket
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtCore/QSocketNotifier-socket-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSocketNotifier.type
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type`
        :description: QtCore/QSocketNotifier-type-f.rst

    .. sip:signal:: PyQt6.QtCore.QSocketNotifier.activated
        :args:
            int
        :description: QtCore/QSocketNotifier-activated-s.rst
