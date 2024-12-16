.. sip:method-description::
    :status: todo
    :pysig: fdb249863d6e7afffdd419cd3319d952
    :realsig: (bool)
    :digest: d2c17e51da7fc946f900425aca6aa15a

Marks this formatter as dirty, prompting the renderer to make a new copy of its cache on the next renderer synchronization. This method should be called by a subclass whenever the formatter is changed in a way that affects the resolved values. Set *labelsChange* to ``true`` if the change requires regenerating the parent axis label strings.
