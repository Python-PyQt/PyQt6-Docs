.. sip:class-description::
    :status: todo
    :brief: Convenience class for grouping remote server endpoints that share common network request properties
    :digest: dbec434a72033d4f7e8fec9b0531a123

Convenience class for grouping remote server endpoints that share common network request properties.

REST servers often have endpoints that require the same headers and other data. Grouping such endpoints with a :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory` makes it more convenient to issue requests to these endpoints; only the typically varying parts such as *path* and *query* parameters are provided when creating a new request.

Basic usage steps of :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory` are as follows:

* Instantiation

* Setting the data common to all requests

* Issuing requests

An example of usage:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkrequestfactory.py
    :lines: 8-17
