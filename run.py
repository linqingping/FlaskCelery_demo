from app import create_app,celery_app

app = create_app()
# 关键点，往celery推入flask信息，使得celery能使用flask上下文
app.app_context().push()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

