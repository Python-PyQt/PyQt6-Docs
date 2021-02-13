.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5d485a1dc288b179c15cf0f5247df778

This method is used to communicate that the response is no longer required by the engine.

It may be reimplemented to cancel a request in the provider side, however, it is not mandatory.

A cancelled :sip:ref:`~PyQt6.QtQuick.QQuickImageResponse` still needs to emit :sip:ref:`~PyQt6.QtQuick.QQuickImageResponse.finished` so that the engine may clean up the :sip:ref:`~PyQt6.QtQuick.QQuickImageResponse`.

**Note:** :sip:ref:`~PyQt6.QtQuick.QQuickImageResponse.finished` should not be emitted until the response is complete, regardless of whether or not  was called. If it is called prematurely, the engine may destroy the response while it is still active, leading to a crash.
