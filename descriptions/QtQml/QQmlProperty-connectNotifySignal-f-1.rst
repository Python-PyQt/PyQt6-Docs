.. sip:method-description::
    :status: todo
    :pysig: 6ce764ff0ff97bf24211cc7e4dcc01f6
    :realsig: (QObject*,int) const
    :digest: 7e3a6779201d77897e3399532de455ad

Connects the property's change notifier signal to the specified *method* of the *dest* object and returns true. Returns false if this metaproperty does not represent a regular Qt property or if it has no change notifier signal, or if the *dest* object does not have the specified *method*.
