from flask import Blueprint, render_template
from evr.models import Cook

bp = Blueprint('cook', __name__, url_prefix='/cook')


@bp.route('/list/')
def _list():
    cook_list = Cook.query.order_by(Cook.id)
    return render_template('cook/cooks.html', cooks=cook_list)

@bp.route('/detail/<int:cook_id>/')
def detail(cook_id):
    cook = Cook.query.get_or_404(cook_id)
    return render_template('cook/cook_detail.html', cook=cook)