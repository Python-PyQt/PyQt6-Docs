.. sip:class-description::
    :status: todo
    :brief: Exposes various network information through native backends
    :digest: 0eabe4564d1ab0c11e3b7f9ff5392154

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` exposes various network information through native backends.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` provides a cross-platform interface to network-related information through plugins.

Various plugins can have various functionality supported, and so you can :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load` plugins based on which features are needed.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` is a singleton and stays alive from the first successful :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load` until destruction of the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object. If you destroy and re-create the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object you must call :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load` again.

**Note:** Because the class is a singleton while also relying on :sip:ref:`~PyQt6.QtCore.QCoreApplication`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` should always first be loaded in the same thread as the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object. This is because the object will also be destroyed in this thread, and various backend-specific components may rely on being destroyed in the same thread as it is created.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`.
