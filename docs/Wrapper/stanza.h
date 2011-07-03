#ifndef stanza_h
#define stanza_h

#include "baseclass.h"

class handler;
class xmlstream;
class event_queue;
class attribute;
class interfaces;
class type;
class xml payload;
class plugin;
class tag;
class value;
class JID;

class stanza : public baseclass {

 public:

    virtual void newOperation();

    virtual void newOperation();

    virtual void newOperation();

 public:
    null index;
    null attribute;
    null to;
    null from;
    null type;
    null is_extension;
    null iterables;
    null name;
    null namespace;
    null parent;
    null overrides;

 public:

    /**
     * @element-type handler
     */
    handler *myhandler;

    /**
     * @element-type xmlstream
     */
    xmlstream *stream;

    /**
     * @element-type event_queue
     */
    event_queue *myevent_queue;

    /**
     * @element-type attribute
     */
    attribute *myattribute;

    /**
     * @element-type interfaces
     */
    interfaces *interfaces;

    /**
     * @element-type type
     */
    type *type;

    /**
     * @element-type xml payload
     */
    xml payload *xml;

    /**
     * @element-type plugin
     */
    plugin *plugins;

    /**
     * @element-type interfaces
     */
    interfaces *sub_interfaces;

    /**
     * @element-type baseclass
     */
    baseclass *subitem;

    /**
     * @element-type tag
     */
    tag *tag;

    /**
     * @element-type type
     */
    type *type;

    /**
     * @element-type type
     */
    type *types;

    /**
     * @element-type value
     */
    value *myvalue;

    /**
     * @element-type value
     */
    value *values;

    /**
     * @element-type JID
     */
    JID *from;

    /**
     * @element-type JID
     */
    JID *to;
};

#endif // stanza_h
