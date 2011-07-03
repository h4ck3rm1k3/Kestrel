#ifndef tag_h
#define tag_h

class plugin;
class stanza;

class tag {

 public:

    /**
     * @element-type plugin
     */
    plugin *tag_map;

    /**
     * @element-type stanza
     */
    stanza *tag;
};

#endif // tag_h
