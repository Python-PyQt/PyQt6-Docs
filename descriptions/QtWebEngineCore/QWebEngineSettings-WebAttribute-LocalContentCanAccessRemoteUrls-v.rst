.. sip:enum-member-description::
    :status: todo
    :value: 6
    :digest: c025a5b884f9a4eba2ddd15e63b00957

Allows locally loaded documents to ignore cross-origin rules so that they can access remote resources that would normally be blocked, since remote resources are considered cross-origin for a local document. Remote access that would not be blocked by cross-origin rules is still possible when this setting is disabled (default). Note that disabling this setting does not prevent media elements in local files from accessing remote content. Disabled by default.
