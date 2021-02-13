.. sip:class-description::
    :status: todo
    :brief: Bundles signals from identifiable senders
    :digest: c0c61682b815de085c08dc2a933da251

The :sip:ref:`~PyQt6.QtCore.QSignalMapper` class bundles signals from identifiable senders.

This class collects a set of parameterless signals, and re-emits them with integer, string or widget parameters corresponding to the object that sent the signal. Note that in most cases you can use lambdas for passing custom parameters to slots. This is less costly and will simplify the code.

The class supports the mapping of particular strings, integers, objects and widgets with particular objects using :sip:ref:`~PyQt6.QtCore.QSignalMapper.setMapping`. The objects' signals can then be connected to the :sip:ref:`~PyQt6.QtCore.QSignalMapper.map` slot which will emit a signal (it could be :sip:ref:`~PyQt6.QtCore.QSignalMapper.mappedInt`, :sip:ref:`~PyQt6.QtCore.QSignalMapper.mappedString` and :sip:ref:`~PyQt6.QtCore.QSignalMapper.mappedObject`) with a value associated with the original signalling object. Mappings can be removed later using :sip:ref:`~PyQt6.QtCore.QSignalMapper.removeMappings`.

Example: Suppose we want to create a custom widget that contains a group of buttons (like a tool palette). One approach is to connect each button's ``clicked()`` signal to its own custom slot; but in this example we want to connect all the buttons to a single slot and parameterize the slot by the button that was clicked.

Here's the definition of a simple custom widget that has a single signal, ``clicked()``, which is emitted with the text of the button that was clicked:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsignalmapper-buttonwidget.py
    :lines: 62-73

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsignalmapper-buttonwidget.py
    :lines: 75-75

The only function that we need to implement is the constructor:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsignalmapper-buttonwidget.py
    :lines: 62-73

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsignalmapper-buttonwidget.py
    :lines: 75-75

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsignalmapper-buttonwidget.py

A list of texts is passed to the constructor. A signal mapper is constructed and for each text in the list a :sip:ref:`~PyQt6.QtWidgets.QPushButton` is created. We connect each button's ``clicked()`` signal to the signal mapper's :sip:ref:`~PyQt6.QtCore.QSignalMapper.map` slot, and create a mapping in the signal mapper from each button to the button's text. Finally we connect the signal mapper's :sip:ref:`~PyQt6.QtCore.QSignalMapper.mappedString` signal to the custom widget's ``clicked()`` signal. When the user clicks a button, the custom widget will emit a single ``clicked()`` signal whose argument is the text of the button the user clicked.

This class was mostly useful before lambda functions could be used as slots. The example above can be rewritten simpler without :sip:ref:`~PyQt6.QtCore.QSignalMapper` by connecting to a lambda function.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsignalmapper-buttonwidget.py

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject`, :sip:ref:`~PyQt6.QtWidgets.QButtonGroup`, :sip:ref:`~PyQt6.QtGui.QActionGroup`.
