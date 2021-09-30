.. sip:module-description::
    :status:    done
    :brief:     Classes for peer-to-peer communication between Python and HTML/JavaScript

The :sip:ref:`~PyQt6.QtWebChannel` module contains classes that enable
peer-to-peer communication between a server (QML/Python application) and a
client (HTML/JavaScript or QML application).  It is supported out of the box by
Qt WebEngine.  In addition it can work on all browsers that support WebSockets,
enabling WebChannel clients to run in any JavaScript environment (including
QML).  This requires the implementation of a custom transport based on
:sip:ref:`~PyQt6.QtWebSockets`.
