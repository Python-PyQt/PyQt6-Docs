.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 881e46ebba88b9dcc4b27060c9261b06

This event is delivered to the item by the scene at some point after it has been constructed, but before it is shown or otherwise accessed through the scene. You can use this event handler to do last-minute initializations of the widget which require the item to be fully constructed.

The base implementation does nothing.
