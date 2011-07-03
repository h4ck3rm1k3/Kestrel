#ifndef threading_h
#define threading_h

class xmlstream;

class threading {

 public:

    virtual void run();

    virtual void __bootstrap_inner();

    virtual void __bootstrap();

    virtual void stream_event_handler_0();

 public:
    String name;

 public:

    /**
     * @element-type xmlstream
     */
    xmlstream *calls;
};

#endif // threading_h
