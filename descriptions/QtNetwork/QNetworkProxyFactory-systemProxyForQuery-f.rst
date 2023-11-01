.. sip:method-description::
    :status: todo
    :pysig: bf63f39e2689939e2d706c51fd0a0e79
    :realsig: (const QNetworkProxyQuery&)
    :digest: 17bb584b19e2a0895779415e54710b48

This function takes the query request, *query*, examines the details of the type of socket or request and returns a list of :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy` objects that indicate the proxy servers to be used, in order of preference.

This function can be used to determine the platform-specific proxy settings. This function will use the libraries provided by the operating system to determine the proxy for a given connection, if such libraries exist. If they don't, this function will just return a :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy` of type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.NoProxy`.

On Windows, this function will use the WinHTTP DLL functions. Despite its name, Microsoft suggests using it for all applications that require network connections, not just HTTP. This will respect the proxy settings set on the registry with the proxycfg.exe tool. If those settings are not found, this function will attempt to obtain Internet Explorer's settings and use them.

On macOS, this function will obtain the proxy settings using the CFNetwork framework from Apple. It will apply the FTP, HTTP and HTTPS proxy configurations for queries that contain the protocol tag "ftp", "http" and "https", respectively. If the SOCKS proxy is enabled in that configuration, this function will use the SOCKS server for all queries. If SOCKS isn't enabled, it will use the HTTPS proxy for all TcpSocket and UrlRequest queries.

On systems configured with libproxy support, this function will rely on libproxy to obtain the proxy settings. Depending on libproxy configurations, this can in turn delegate to desktop settings, environment variables, etc.

On other systems, this function will pick up proxy settings from the "http_proxy" environment variable. This variable must be a URL using one of the following schemes: "http", "socks5" or "socks5h".

Limitations
-----------

These are the limitations for the current version of this function. Future versions of Qt may lift some of the limitations listed here.

* On Windows platforms, this function may take several seconds to execute depending on the configuration of the user's system.
