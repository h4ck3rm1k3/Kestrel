#ifndef Kestrel_manager_h
#define Kestrel_manager_h

#include "pool.h"

class xmlstream;

class Kestrel_manager {

 public:

    virtual void clean_pool();

    virtual void start();

    virtual void clean_tasks();

 public:
    Integer transaction_count;

 public:

    /**
     * @element-type pool
     */
    pool pool;

    /**
     * @element-type xmlstream
     */
    xmlstream *event runner calls start;
};

#endif // Kestrel_manager_h
