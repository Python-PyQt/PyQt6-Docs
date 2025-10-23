.. sip:class-description::
    :status: todo
    :brief: Exposes various network information through native backends
    :digest: bc8e9b04357e6fdb74d04dbb6c0910fa

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` exposes various network information through native backends.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` provides a cross-platform interface to network-related information through plugins.

Various plugins can have various functionality supported, and so you can load plugins based on which features are needed.

In most cases, the recommended approach is to load the platform-specific backend by calling :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.loadDefaultBackend`. This will automatically select the most appropriate backend available on the current platform and is suitable for the majority of applications.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qnetworkinformation.py

For more advanced uses cases, developers may prefer to load a backend based on specific capabilities or preferences. :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.loadBackendByFeatures` allows selecting a backend that supports a specific set of features, such as reporting the transport mediom or signal strength. Alternatively, :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.loadBackendByName` allows loading a plugin by its name, which can include platform-specific or custom backend implementations.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` is a singleton and stays alive from the first successful load until destruction of the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object. If you destroy and re-create the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object you must load it again to reinitialize the plugin.

**Note:** Because the class is a singleton while also relying on :sip:ref:`~PyQt6.QtCore.QCoreApplication`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` should always first be loaded in the same thread as the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object. This is because the object will also be destroyed in this thread, and various backend-specific components may rely on being destroyed in the same thread as it is created.

One possible use case for :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation` is to monitor network connectivity status. :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.reachability` provides an indication of whether the system is considered online, based on information reported by the underlying operating system or plugin. However, this information may not always be accurate. For example, on Windows, the online check may rely on connectivity to a Microsoft-owned server; if that server is unreachable (e.g., due to firewall rules), the system may incorrectly report that it is offline. As such, :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.reachability` should not be used as a definitive pre-check before attempting a network connection, but rather as a general signal of connectivity state.

To use :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.reachability` effectively, the application must also understand what kind of destination it is trying to reach. For example, if the target is a local IP address, then :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability.Local` or :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability.Site` may be sufficient. If the destination is on the public internet, then :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability.Online` is required. Without this context, interpretring the reported reachability may lead to incorrect assumptions about actual network access.

**Warning:** Only Linux and Windows provide support for the finer-grained :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability.Site` and :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Reachability.Local` options. On Android and Apple platforms :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.reachability` is limited to reporting only Online, Offline or Unknown. Therefore, any logic that relies on detecting Local or Site level connectivity must include appropriate platform checks or fallbacks.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qnetworkinformation_reachability.py
    :lines: 13-24

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qnetworkinformation_reachability.py
    :lines: 36-64

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature`.
