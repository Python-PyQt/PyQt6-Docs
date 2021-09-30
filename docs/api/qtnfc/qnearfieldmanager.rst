:orphan:

.. sip:class:: PyQt6.QtNfc.QNearFieldManager
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNfc/QNearFieldManager-c.rst

    .. sip:enum:: PyQt6.QtNfc.QNearFieldManager.AdapterState
        :description: QtNfc/QNearFieldManager-AdapterState-e.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldManager.AdapterState.Offline
            :description: QtNfc/QNearFieldManager-AdapterState-Offline-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldManager.AdapterState.Online
            :description: QtNfc/QNearFieldManager-AdapterState-Online-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldManager.AdapterState.TurningOff
            :description: QtNfc/QNearFieldManager-AdapterState-TurningOff-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldManager.AdapterState.TurningOn
            :description: QtNfc/QNearFieldManager-AdapterState-TurningOn-v.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldManager.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNfc/QNearFieldManager-__init__-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldManager.isEnabled
        :returns:
            bool
        :description: QtNfc/QNearFieldManager-isEnabled-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldManager.isSupported
        :args:
            accessMethod: :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.AccessMethod` = :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.AccessMethod.AnyAccess`
        :returns:
            bool
        :description: QtNfc/QNearFieldManager-isSupported-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldManager.setUserInformation
        :args:
            str
        :description: QtNfc/QNearFieldManager-setUserInformation-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldManager.startTargetDetection
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.AccessMethod`
        :returns:
            bool
        :description: QtNfc/QNearFieldManager-startTargetDetection-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldManager.stopTargetDetection
        :args:
            errorMessage: str = ''
        :description: QtNfc/QNearFieldManager-stopTargetDetection-f.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldManager.adapterStateChanged
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.AdapterState`
        :description: QtNfc/QNearFieldManager-adapterStateChanged-s.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldManager.targetDetected
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget`
        :description: QtNfc/QNearFieldManager-targetDetected-s.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldManager.targetDetectionStopped
        :description: QtNfc/QNearFieldManager-targetDetectionStopped-s.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldManager.targetLost
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget`
        :description: QtNfc/QNearFieldManager-targetLost-s.rst
