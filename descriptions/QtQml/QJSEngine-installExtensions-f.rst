.. sip:method-description::
    :status: todo
    :pysig: 75300c0e4ebfecfb3bada28f6a242ae6
    :realsig: (QJSEngine::Extensions, const QJSValue&)
    :digest: 65a2f29b85f16473e2c477084882e6c2

Installs JavaScript *extensions* to add functionality that is not available in a standard ECMAScript implementation.

The extensions are installed on the given *object*, or on the :sip:ref:`~PyQt6.QtQml.QJSEngine.globalObject` if no object is specified.

Several extensions can be installed at once by ``OR``-ing the enum values:

::

    installExtensions(QJSEngine::TranslationExtension | QJSEngine::ConsoleExtension);

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.Extension.Extension`.
