.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: bbc782f5dd8f9873379f53cf5fce157e

The object is owned by JavaScript. When the object is returned to the JavaScript memory manager as the return value of a method call, the JavaScript memory manager will track it and delete it if there are no remaining JavaScript references to it and it has no :sip:ref:`~PyQt6.QtCore.QObject.parent`. An object tracked by one :sip:ref:`~PyQt6.QtQml.QJSEngine` will be deleted during that :sip:ref:`~PyQt6.QtQml.QJSEngine`'s destructor. Thus, JavaScript references between objects with  from two different engines will not be valid if one of these engines is deleted. This option is similar to QScriptEngine::ScriptOwnership.
