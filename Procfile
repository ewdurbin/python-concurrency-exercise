http_prefork: gunicorn -w 2 --access-logfile - --error-logfile - app:app
http_threaded: gunicorn -w 2 -k gunicorn.workers.gthread.ThreadWorker --access-logfile - --error-logfile - app:app
http_evented: gunicorn -w 2 -k gunicorn.workers.gaiohttp.AiohttpWorker --access-logfile - --error-logfile - app:app
nginx: nginx -c $PWD/nginx.conf
