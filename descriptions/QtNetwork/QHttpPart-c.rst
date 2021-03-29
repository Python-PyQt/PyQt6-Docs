.. sip:class-description::
    :status: todo
    :brief: Holds a body part to be used inside a HTTP multipart MIME message
    :digest: 412016e8d789b984ed20f6d51c04eae7

The :sip:ref:`~PyQt6.QtNetwork.QHttpPart` class holds a body part to be used inside a HTTP multipart MIME message.

The :sip:ref:`~PyQt6.QtNetwork.QHttpPart` class holds a body part to be used inside a HTTP multipart MIME message (which is represented by the :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart` class). A :sip:ref:`~PyQt6.QtNetwork.QHttpPart` consists of a header block and a data block, which are separated by each other by two consecutive new lines. An example for one part would be:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qhttppart.py
    :lines: 43-46

For setting headers, use :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setHeader` and :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setRawHeader`, which behave exactly like :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setHeader` and :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setRawHeader`.

For reading small pieces of data, use :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBody`; for larger data blocks like e.g. images, use :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`. The latter method saves memory by not copying the data internally, but reading directly from the device. This means that the device must be opened and readable at the moment when the multipart message containing the body part is sent on the network via :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`.

To construct a :sip:ref:`~PyQt6.QtNetwork.QHttpPart` with a small body, consider the following snippet (this produces the data shown in the example above):

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qhttppart.py
    :lines: 50-53

To construct a :sip:ref:`~PyQt6.QtNetwork.QHttpPart` reading from a device (e.g. a file), the following can be applied:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qhttppart.py
    :lines: 57-63

Be aware that :sip:ref:`~PyQt6.QtNetwork.QHttpPart` does not take ownership of the device when set, so it is the developer's responsibility to destroy it when it is not needed anymore. A good idea might be to set the multipart message as parent object for the device, as documented at the documentation for :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.
