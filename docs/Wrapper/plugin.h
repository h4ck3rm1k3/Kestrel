#ifndef plugin_h
#define plugin_h

#include "baseclass.h"

class stanza;
class tag;

class plugin : public baseclass {

 public:
    null attrib;
    null atrrib_map;
    null tag_map;

 public:

    /**
     * @element-type stanza
     */
    stanza *plugins;

    /**
     * @element-type tag
     */
    tag *tag_map;
};

#endif // plugin_h
