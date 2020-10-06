# ACC_lab3
A very basic web service with task queue system at backend to provide scalable solution.

## Web service
- `twitter.py`: Provides several routes to functions;  
- `templates`/`index.html`: Very basic webpage, HTML + JavaScript (jQurey & Chart.js).

## Task queue
- `celeryconfig.py`: Configuration of the broker and result backend;  
- `tasks.py`: The tweet analyzing task;  
- `redis.config`: Configuration of the redis server.

## Contextualization
- `contextualization`/`master.sh`: Settings needed for the master node (just a note, not for running);  
- `contextualization`/`worker`/`create_key_pair.py`: Register the public key of the new master node;  
- `contextualization`/`worker`/`ssc-instance-userdata.py`: Provision a worker that the master can directly ssh;
- `contextualization`/`worker`/`cloud-cfg.txt`: Contextualize the new worker node with celery.
