from flask import request
from littlebrother import app

def paginate(sq):
    total_count = sq.count()
    page = int(request.args.get('page', 1))
    sq = sq.paginate(page, app.config['RESULTS_PER_PAGE'])
    return dict(
        voters=sq,
        total_voters_count=total_count,
        has_next_page=(page * app.config['RESULTS_PER_PAGE']) < total_count,
        next_page_num=page + 1,
    )
