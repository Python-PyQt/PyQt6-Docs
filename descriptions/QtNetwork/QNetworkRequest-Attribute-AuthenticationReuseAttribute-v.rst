.. sip:enum-member-description::
    :status: todo
    :value: 12
    :digest: 3cfcb1374871d5e24b74ac558aa2a7a9

Requests only, type: :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Int` (default: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.LoadControl.Automatic`) Indicates whether to use cached authorization credentials in the request, if available. If this is set to :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.LoadControl.Manual` and the authentication mechanism is 'Basic' or 'Digest', Qt will not send an an 'Authorization' HTTP header with any cached credentials it may have for the request's URL. This attribute is set to :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.LoadControl.Manual` by Qt WebKit when creating a cross-origin `XMLHttpRequest <https://doc.qt.io/qt-6/qml-qtqml-xmlhttprequest.html>`_ where withCredentials has not been set explicitly to true by the Javascript that created the request. See `here <http://www.w3.org/TR/XMLHttpRequest2/#credentials-flag>`_ for more information. (This value was introduced in 4.7.)
