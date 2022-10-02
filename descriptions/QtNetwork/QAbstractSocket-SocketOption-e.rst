.. sip:enum-description::
    :status: todo
    :digest: 1b8ce2cab59781781bcbdcce46b8b6ea

This enum represents the options that can be set on a socket. If desired, they can be set after having received the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connected` signal from the socket or after having received a new socket from a :sip:ref:`~PyQt6.QtNetwork.QTcpServer`.

Possible values for *TypeOfServiceOption* are:

+-------+----------------------+
| Value | Description          |
+=======+======================+
| 224   | Network control      |
+-------+----------------------+
| 192   | Internetwork control |
+-------+----------------------+
| 160   | CRITIC/ECP           |
+-------+----------------------+
| 128   | Flash override       |
+-------+----------------------+
| 96    | Flash                |
+-------+----------------------+
| 64    | Immediate            |
+-------+----------------------+
| 32    | Priority             |
+-------+----------------------+
| 0     | Routine              |
+-------+----------------------+

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setSocketOption`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.socketOption`.
