:orphan:

.. sip:class:: PyQt6.QtQml.QQmlIncubator
    :description: QtQml/QQmlIncubator-c.rst

    .. sip:enum:: PyQt6.QtQml.QQmlIncubator.IncubationMode
        :description: QtQml/QQmlIncubator-IncubationMode-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlIncubator.IncubationMode.Asynchronous
            :description: QtQml/QQmlIncubator-IncubationMode-Asynchronous-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested
            :description: QtQml/QQmlIncubator-IncubationMode-AsynchronousIfNested-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlIncubator.IncubationMode.Synchronous
            :description: QtQml/QQmlIncubator-IncubationMode-Synchronous-v.rst

    .. sip:enum:: PyQt6.QtQml.QQmlIncubator.Status
        :description: QtQml/QQmlIncubator-Status-e.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlIncubator.Status.Error
            :description: QtQml/QQmlIncubator-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlIncubator.Status.Loading
            :description: QtQml/QQmlIncubator-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlIncubator.Status.Null
            :description: QtQml/QQmlIncubator-Status-Null-v.rst

        .. sip:enum-member:: PyQt6.QtQml.QQmlIncubator.Status.Ready
            :description: QtQml/QQmlIncubator-Status-Ready-v.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.__init__
        :args:
            mode: :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode` = :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.Asynchronous`
        :description: QtQml/QQmlIncubator-__init__-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.clear
        :description: QtQml/QQmlIncubator-clear-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.errors
        :returns:
            List[:sip:ref:`~PyQt6.QtQml.QQmlError`]
        :description: QtQml/QQmlIncubator-errors-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.forceCompletion
        :description: QtQml/QQmlIncubator-forceCompletion-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.incubationMode
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode`
        :description: QtQml/QQmlIncubator-incubationMode-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.isError
        :returns:
            bool
        :description: QtQml/QQmlIncubator-isError-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.isLoading
        :returns:
            bool
        :description: QtQml/QQmlIncubator-isLoading-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.isNull
        :returns:
            bool
        :description: QtQml/QQmlIncubator-isNull-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.isReady
        :returns:
            bool
        :description: QtQml/QQmlIncubator-isReady-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.object
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QQmlIncubator-object-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.setInitialProperties
        :args:
            Dict[str, Any]
        :description: QtQml/QQmlIncubator-setInitialProperties-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.setInitialState
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QQmlIncubator-setInitialState-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.status
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlIncubator.Status`
        :description: QtQml/QQmlIncubator-status-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlIncubator.statusChanged
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlIncubator.Status`
        :description: QtQml/QQmlIncubator-statusChanged-f.rst
