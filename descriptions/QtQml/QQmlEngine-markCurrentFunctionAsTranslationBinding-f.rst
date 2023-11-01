.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e1a5d3d3285225d751b1d337a62bcfa3

If this method is called inside of a function that is part of a binding in QML, the binding will be treated as a translation binding.

::

    class I18nAwareClass : public QObject {

      //...

       QString text() const
       {
            if (auto engine = qmlEngine(this))
                engine->markCurrentFunctionAsTranslationBinding();
            return tr("Hello, world!");
       }
    };

**Note:** This function is mostly useful if you wish to provide your own alternative to the qsTr function. To ensure that properties exposed from C++ classes are updated on language changes, it is instead recommended to react to ``LanguageChange`` events. That is a more general mechanism which also works when the class is used in a non-QML context, and has slightly less overhead. However, using ``markCurrentFunctionAsTranslationBinding`` can be acceptable when the class is already closely tied to the QML engine. For more details, see Prepare for Dynamic Language Changes

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.retranslate`.
