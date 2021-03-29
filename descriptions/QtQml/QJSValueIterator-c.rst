.. sip:class-description::
    :status: todo
    :brief: Java-style iterator for QJSValue
    :digest: fc07dc3fade127ed3fcbddd28cecb90c

The :sip:ref:`~PyQt6.QtQml.QJSValueIterator` class provides a Java-style iterator for :sip:ref:`~PyQt6.QtQml.QJSValue`.

The :sip:ref:`~PyQt6.QtQml.QJSValueIterator` constructor takes a :sip:ref:`~PyQt6.QtQml.QJSValue` as argument. After construction, the iterator is located at the very beginning of the sequence of properties. Here's how to iterate over all the properties of a :sip:ref:`~PyQt6.QtQml.QJSValue`:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsvalueiterator.py
    :lines: 54-60

The :sip:ref:`~PyQt6.QtQml.QJSValueIterator.next` advances the iterator. The :sip:ref:`~PyQt6.QtQml.QJSValueIterator.name` and :sip:ref:`~PyQt6.QtQml.QJSValueIterator.value` functions return the name and value of the last item that was jumped over.

Note that :sip:ref:`~PyQt6.QtQml.QJSValueIterator` only iterates over the :sip:ref:`~PyQt6.QtQml.QJSValue`'s own properties; i.e. it does not follow the prototype chain. You can use a loop like this to follow the prototype chain:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsvalueiterator.py
    :lines: 65-73

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.property`.
