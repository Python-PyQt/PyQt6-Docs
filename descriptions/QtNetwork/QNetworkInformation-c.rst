.. sip:class-description::
    :status: todo
    :brief: Exposes various network information through native backends
    :digest: 139835cbf52f1272c643b27574927db9

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` exposes various network information through native backends.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` provides a cross-platform interface to network-related information through plugins.

Various plugins can have various functionality supported, and so you can :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load` plugins based on which features are needed.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` is a singleton and stays alive from the first successful :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load` until destruction of the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object. If you destroy and re-create the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object you must call :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load` again.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`.
