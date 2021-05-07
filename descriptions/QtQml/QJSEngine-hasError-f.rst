.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 74aaf72519ea01cf5a7a56495041bb7a

Returns ``true`` if the last JavaScript execution resulted in an exception or if :sip:ref:`~PyQt6.QtQml.QJSEngine.throwError` was called. Otherwise returns ``false``. Mind that :sip:ref:`~PyQt6.QtQml.QJSEngine.evaluate` catches any exceptions thrown in the evaluated code.
