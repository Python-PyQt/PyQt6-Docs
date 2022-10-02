.. sip:class-description::
    :status: todo
    :brief: Exposes various network information through native backends
    :digest: 42bb6b134553410c83d8d7373e1c36ec

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` exposes various network information through native backends.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` provides a cross-platform interface to network-related information through plugins.

Various plugins can have various functionality supported, and so you can load() plugins based on which features are needed.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` is a singleton and stays alive from the first successful load() until destruction of the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object. If you destroy and re-create the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object you must call load() again.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`.
