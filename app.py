from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


tasks = [
    {'id': 1, 'text': 'Купить продукты', 'done': False, 'date': '2026-06-01', 'priority': 'высокий'},
    {'id': 2, 'text': 'Сделать домашнее задание', 'done': False, 'date': '2026-06-05', 'priority': 'высокий'},
    {'id': 3, 'text': 'Позвонить маме', 'done': True, 'date': '2026-05-28', 'priority': 'средний'},
    {'id': 4, 'text': 'Записаться к врачу', 'done': False, 'date': '2026-06-10', 'priority': 'низкий'},
    {'id': 5, 'text': 'Прочитать книгу', 'done': False, 'date': '2026-06-02', 'priority': 'средний'},
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/search')
def search():
    query = request.args.get('q', '').strip().lower()
    if query:
        filtered_tasks = [task for task in tasks if query in task['text'].lower()]
    else:
        filtered_tasks = tasks
    return render_template('index.html', tasks=filtered_tasks, search_query=query)


@app.route('/sort/date')
def sort_by_date():
    sorted_tasks = sorted(tasks, key=lambda t: t.get('date', ''), reverse=True)
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/sort/status')
def sort_by_status():
    sorted_tasks = sorted(tasks, key=lambda t: t.get('done', False))
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/sort/priority')
def sort_by_priority():
    priority_order = {'высокий': 1, 'средний': 2, 'низкий': 3}
    sorted_tasks = sorted(
        tasks,
        key=lambda t: priority_order.get(t.get('priority', 'средний'), 2)
    )
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/sort/alpha')
def sort_by_alpha():
    sorted_tasks = sorted(tasks, key=lambda t: t.get('text', '').lower())
    return render_template('index.html', tasks=sorted_tasks)

if __name__ == '__main__':
    app.run(debug=True)
