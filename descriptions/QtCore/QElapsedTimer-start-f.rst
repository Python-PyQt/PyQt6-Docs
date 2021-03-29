.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 56bae2219cf6443ab604317a5bf0d3b9

Starts this timer. Once started, a timer value can be checked with :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed` or :sip:ref:`~PyQt6.QtCore.QElapsedTimer.msecsSinceReference`.

Normally, a timer is started just before a lengthy operation, such as:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qelapsedtimer-main.py

Also, starting a timer makes it valid again.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.restart`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.invalidate`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed`.
