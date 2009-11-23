from django.conf import settings
from django.db import connection
from django.template import Template, Context

import logger

class SQLLogMiddleware:

    def process_response ( self, request, response ):
        if not settings.LOG_SQL: return response

        query_count = len(connection.queries)
        time = 0.0
        for q in connection.queries:
            time += float(q['time'])

        if settings.LOG_SQL_TO_RESPONSE and query_count > 0:
            t = Template('''
                <div class='sqllog'>
                <p><em>Total query count:</em> {{ count }}<br/>
                <em>Total execution time:</em> {{ time }}</p>
                <ul>
                    {% for sql in sqllog %}
                        <li><em>{{ sql.time }}</em>: {{ sql.sql }}</li>
                    {% endfor %}
                </ul>
                </div>
            ''')

            content = t.render(Context({
                'sqllog': connection.queries,
                'count': query_count,
                'time': time
            }))
            response.content = "%s%s" % (response.content, content,)

        if settings.LOG_SQL_TO_FILE and query_count > 0:
            logger.sql.info( "Total execution time: %s" %  time )
            logger.sql.info( "Total query count: %s" % query_count )
            for query in connection.queries:
                logger.sql.info( "(%s) : %s" % (query['time'], query['sql']) )

        return response
