.. sip:method-description::
    :status: todo
    :pysig: a97d54dac19747494af6afe8dd452514
    :realsig: (const QNetworkRequest&,const QWebSocketHandshakeOptions&)
    :digest: 59b7f48a064b0ebf58c9cbe9f0513692

Opens a WebSocket connection using the given *request* and *options*.

The *request* url will be used to open the WebSocket connection. Headers present in the request will be sent to the server in the upgrade request, together with the ones needed for the websocket handshake.

Additional options for the WebSocket handshake such as subprotocols can be specified in *options*.
